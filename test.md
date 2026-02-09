# Testing Guide for Netfix

Follow these steps to run and verify the project's functionality.

## 1. Setup and Run
Ensure you have Django installed and the database migrated:
```bash
pip install "Django==3.1.14"
python3 manage.py migrate
python3 manage.py runserver
```
The site will be available at `http://127.0.0.1:8000/`.

## 2. Functional Test Checklist

### A. User Registration & Profile
1.  **Register a Customer**:
    - Go to `/users/register/customer/`.
    - Fill in username, email, password, and birth date.
    - **Verify**: You are redirected to your profile and see your birth date.
2.  **Register a Company**:
    - Logout and go to `/users/register/company/`.
    - Select a field of work (e.g., `Electricity`).
    - **Verify**: You are redirected to your profile and see your field of work.
3.  **Unique Constraints**:
    - Try to register another user with the same email or username.
    - **Verify**: The system prevents registration and shows an error.

### B. Service Management
1.  **Create a Service (as Company)**:
    - Logged in as the `Electricity` company, go to `/services/create/`.
    - **Verify**: The "Field" dropdown is restricted to `Electricity` only.
2.  **Verify Service in Profile**:
    - After creating, check your Company Profile.
    - **Verify**: The new service appears in your "Services Provided" list.

### C. Discovery & Requests
1.  **Browse Services**:
    - Go to `All Services` or `Trending`.
    - **Verify**: The created service appears in the list.
2.  **Request a Service (as Customer)**:
    - Login as a Customer.
    - View the detail page of the Electricity service.
    - Click "Request Service", enter an address and 2 hours.
3.  **Verify Calculation**:
    - Go to the Customer Profile.
    - **Verify**: The requested service appears in the history.
    - **Verify**: If price was 10.50 and hours were 2, the cost displays as **21.00**.

### D. Trending Services
1.  **Most Requested**:
    - Request the same service multiple times or with different customers.
    - Go to the `Trending` page.
    - **Verify**: The service with the most requests appears at the top.

## 3. Automated Tests (Optional)
You can also run Django's test runner if you add unit tests in `tests.py` files:
```bash
python3 manage.py test
```
