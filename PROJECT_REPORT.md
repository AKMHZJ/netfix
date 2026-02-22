# Netfix Project Report

## Project Overview
Netfix is a service marketplace web application where companies can offer services (like plumbing, painting, etc.) and customers can request them.

## Technologies Used
- **Language**: Python 3
- **Framework**: Django 3.1.14
- **Database**: SQLite (Default)
- **Frontend**: HTML5, CSS3 (Django Templates)

## Core Concepts Implemented

### 1. Database Models (ORM)
- **User Extension**: Used `OneToOneField` to link `User` model to `Customer` and `Company` profiles, allowing for role-specific data.
- **Service**: Represents a service offered by a company. Includes constraints (choices) for the "Field of Work".
- **ServiceRequest**: Represents a transaction/request between a Customer and a Service.

### 2. Authentication & Authorization
- **Registration**: Custom forms (`CustomerSignUpForm`, `CompanySignUpForm`) handling multiple models transactionally.
- **Login/Logout**: Utilized Django's built-in auth views.
- **Access Control**: Used `LoginRequiredMixin` and `UserPassesTestMixin` to restrict views (e.g., only Companies can create services).

### 3. Forms
- **ModelForms**: Used for Service creation and Service Requests to auto-generate HTML and handle validation.
- **Custom Logic**: Implemented dynamic filtering in `ServiceForm` to restrict companies to their field of work (unless "All in One").

### 4. Views (CBVs)
- **Class-Based Views**: Used `CreateView`, `ListView`, `DetailView`, `TemplateView` for cleaner code structure.
- **Context Data**: customized `get_context_data` to pass dynamic information (like aggregation for most requested services).

### 5. Templates & Navigation
- **Inheritance**: Used `base.html` for a consistent layout (navigation, styling).
- **Template Tags**: Used `{% url %}`, `{% if %}`, `{% for %}` for dynamic content rendering.
- **Improved Navigation**: Added direct links to service categories from service listings and details, enhancing discoverability.

### 6. Testing
- **Automated Tests**: Added `services/tests.py` to verify critical business logic:
    - Customer registration flow.
    - Company service creation restrictions (e.g., Plumbers can only create Plumbing services).
    - "All in One" company privileges.
    - Service request cost calculation.

## How to Run
1. **Install Dependencies**:
   ```bash
   pip install django==3.1.14
   ```
2. **Apply Migrations**:
   ```bash
   python3 manage.py migrate
   ```
3. **Run Tests**:
   ```bash
   python3 manage.py test services.tests
   ```
4. **Run Server**:
   ```bash
   python3 manage.py runserver
   ```
5. **Access**: Open `http://127.0.0.1:8000/` in your browser.

## Features
- **User Roles**: Separate registration for Companies and Customers.
- **Service Management**: Companies can create services (restricted by their field).
- **Service Discovery**: Browse by category, view all, or see trending (most requested) services.
- **Request System**: Customers can book services, specifying address and hours.
- **Profiles**: detailed profiles showing history (for customers) or portfolio (for companies).
