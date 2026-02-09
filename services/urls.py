from django.urls import path
from .views import (
    CreateServiceView, ServiceListView, ServiceDetailView,
    RequestServiceView, MostRequestedServicesView, ServicesByCategoryView
)

urlpatterns = [
    path('create/', CreateServiceView.as_view(), name='create_service'),
    path('list/', ServiceListView.as_view(), name='service_list'),
    path('most_requested/', MostRequestedServicesView.as_view(), name='most_requested'),
    path('category/<str:category>/', ServicesByCategoryView.as_view(), name='services_by_category'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('<int:pk>/request/', RequestServiceView.as_view(), name='request_service'),
]
