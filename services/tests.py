from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Customer, Company
from services.models import Service, ServiceRequest
import datetime

class NetfixTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create Customer user
        self.customer_user = User.objects.create_user(username='cust', email='cust@example.com', password='password123')
        # We need a Customer profile for it
        Customer.objects.create(user=self.customer_user, birth_date=datetime.date(1990, 1, 1))
        
        # Create Company (Plumbing) user
        self.plumber_user = User.objects.create_user(username='plumber', email='plumber@example.com', password='password123')
        self.plumber_company = Company.objects.create(user=self.plumber_user, field='Plumbing')
        
        # Create Company (All in One) user
        self.aio_user = User.objects.create_user(username='aio', email='aio@example.com', password='password123')
        self.aio_company = Company.objects.create(user=self.aio_user, field='All in One')

    def test_customer_registration_view(self):
        # Just check if the page loads
        response = self.client.get(reverse('register_customer'))
        self.assertEqual(response.status_code, 200)

    def test_service_creation_restriction_plumber(self):
        self.client.force_login(self.plumber_user)
        
        # 1. Try to create Plumbing service (Should Succeed)
        data = {
            'name': 'Fix Pipe',
            'description': 'Fixing pipes',
            'field': 'Plumbing',
            'price_per_hour': 50.00
        }
        response = self.client.post(reverse('create_service'), data)
        # Assuming success redirects to profile
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Service.objects.filter(name='Fix Pipe').exists())

        # 2. Try to create Painting service (Should Fail)
        data_fail = {
            'name': 'Paint Wall',
            'description': 'Painting walls',
            'field': 'Painting',
            'price_per_hour': 50.00
        }
        response = self.client.post(reverse('create_service'), data_fail)
        self.assertEqual(response.status_code, 200) # Form error, re-renders page
        self.assertFalse(Service.objects.filter(name='Paint Wall').exists())
        self.assertFormError(response, 'form', 'field', 'Select a valid choice. Painting is not one of the available choices.')

    def test_service_creation_all_in_one(self):
        self.client.force_login(self.aio_user)
        
        # 1. Try to create Plumbing service (Should Succeed)
        data = {
            'name': 'AIO Pipe',
            'description': 'Fixing pipes',
            'field': 'Plumbing',
            'price_per_hour': 60.00
        }
        response = self.client.post(reverse('create_service'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Service.objects.filter(name='AIO Pipe').exists())

        # 2. Try to create Painting service (Should Succeed)
        data2 = {
            'name': 'AIO Paint',
            'description': 'Painting walls',
            'field': 'Painting',
            'price_per_hour': 60.00
        }
        response = self.client.post(reverse('create_service'), data2)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Service.objects.filter(name='AIO Paint').exists())

    def test_service_request_flow(self):
        # Setup: Create a service
        service = Service.objects.create(
            name='Leak Fix',
            description='Fixing leak',
            field='Plumbing',
            price_per_hour=100.00,
            company=self.plumber_company
        )

        self.client.force_login(self.customer_user)
        
        # Request the service
        data = {
            'address': '123 Test St',
            'service_hours': 2
        }
        response = self.client.post(reverse('request_service', args=[service.pk]), data)
        
        self.assertEqual(response.status_code, 302) # Redirects to profile
        self.assertTrue(ServiceRequest.objects.filter(service=service, customer__user=self.customer_user).exists())
        
        req = ServiceRequest.objects.get(service=service)
        self.assertEqual(req.cost, 200.00)
