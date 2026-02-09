from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Service, ServiceRequest
from .forms import ServiceForm, ServiceRequestForm
from django.db.models import Count

class CreateServiceView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/create_service.html'

    def test_func(self):
        return hasattr(self.request.user, 'company')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['company'] = self.request.user.company
        return kwargs

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)

    def get_success_url(self):
        return '/users/profile/'

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    ordering = ['-created']
    paginate_by = 10

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'

class RequestServiceView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'services/request_service.html'

    def test_func(self):
        return hasattr(self.request.user, 'customer')

    def dispatch(self, request, *args, **kwargs):
        self.service = get_object_or_404(Service, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        form.instance.service = self.service
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = self.service
        return context

    def get_success_url(self):
        return '/users/profile/'

class MostRequestedServicesView(ListView):
    model = Service
    template_name = 'services/most_requested.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.annotate(num_requests=Count('requests')).order_by('-num_requests')

class ServicesByCategoryView(ListView):
    model = Service
    template_name = 'services/services_by_category.html'
    context_object_name = 'services'

    def get_queryset(self):
        category = self.kwargs.get('category')
        return Service.objects.filter(field=category).order_by('-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs.get('category')
        return context