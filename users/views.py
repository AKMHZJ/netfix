from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer, Company
from .forms import CustomerSignUpForm, CompanySignUpForm

class CustomerSignUpView(CreateView):
    model = Customer
    form_class = CustomerSignUpForm
    template_name = 'users/register_customer.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')

class CompanySignUpView(CreateView):
    model = Company
    form_class = CompanySignUpForm
    template_name = 'users/register_company.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get('user')
        if username:
            user = get_object_or_404(User, username=username)
        else:
            user = self.request.user
            
        context['profile_user'] = user # distinct from request.user
        
        if hasattr(user, 'customer'):
            context['is_customer'] = True
            context['customer'] = user.customer
            context['requests'] = user.customer.requests.all().order_by('-requested_at')
        elif hasattr(user, 'company'):
            context['is_company'] = True
            context['company'] = user.company
            context['services'] = user.company.services.all().order_by('-created')
        return context