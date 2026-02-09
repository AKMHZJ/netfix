from django.db import models
from users.models import Company, Customer

class Service(models.Model):
    FIELD_CHOICES = [
        ('Air Conditioner', 'Air Conditioner'),
        ('Carpentry', 'Carpentry'),
        ('Electricity', 'Electricity'),
        ('Gardening', 'Gardening'),
        ('Home Machines', 'Home Machines'),
        ('Housekeeping', 'Housekeeping'),
        ('Interior Design', 'Interior Design'),
        ('Locks', 'Locks'),
        ('Painting', 'Painting'),
        ('Plumbing', 'Plumbing'),
        ('Water Heaters', 'Water Heaters'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    field = models.CharField(max_length=50, choices=FIELD_CHOICES)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='requests')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='requests')
    address = models.CharField(max_length=200)
    service_hours = models.IntegerField()
    requested_at = models.DateTimeField(auto_now_add=True)

    @property
    def cost(self):
        return self.service.price_per_hour * self.service_hours