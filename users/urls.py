from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomerSignUpView, CompanySignUpView, ProfileView

urlpatterns = [
    path('register/customer/', CustomerSignUpView.as_view(), name='register_customer'),
    path('register/company/', CompanySignUpView.as_view(), name='register_company'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
