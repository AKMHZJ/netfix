# Audit Answers

## Functional

### Register a new Customer.
> When registering a Customer, does the website request a username, an email, a password, a password confirmation and a date of birth?

Yes, the `CustomerSignUpForm` includes `email` and `birth_date` along with the standard `UserCreationForm` fields (username, password, password confirmation).

### Register a new electricity Company.
> When registering a Company, does the website request a username, an email, a password, a password confirmation and a field of work?

Yes, the `CompanySignUpForm` includes `email` and `field` along with the standard `UserCreationForm` fields.

> Is the field of work restricted in a way that it only accepts one of the following values: Air Conditioner, All in One, Carpentry, Electricity, Gardening, Home Machines, Housekeeping, Interior Design, Locks, Painting, Plumbing, Water Heaters?

Yes, the `Company` model uses `FIELD_CHOICES` which restricts the field to these specific values.

> Are you able to register two different types of users (Customers and Companies)?

Yes, there are separate registration views and URLs for Customers and Companies.

### User Uniqueness
> Try to register a new user (Customer or Company) and use a username that already exists. Were you warned that a user with that username already exists?

Yes, the form validation (`clean_username`) checks for existing usernames and raises a `ValidationError`.

> Try to register a new user (Customer or Company) and use an email that already exists. Were you warned that a user with that email already exists?

Yes, the form validation (`clean_email`) checks for existing emails and raises a `ValidationError`.

### Company Profile & Service Creation
> After registering and logging in with a Company profile, navigate to the profile page. Is all its information available (apart from the password)?

Yes, the profile page displays the username, email, and field of work.

> While logged in with the electricity Company, create a new service with a price per hour of 10.50. Were you asked for a name, a description, a price and a field?

Yes, the `CreateServiceView` uses `ServiceForm` which asks for these fields.

> Naviagate to the user (Company) profile. Did the service created before, appears in the company page as an available service?

Yes, the profile page lists all services created by the company.

### Service Listing
> Is there a page showing every service created by every company?

Yes, the `ServiceListView` (URL `/services/list/`) displays all services.

> Is there a page for every type of service which displays every service of that type?

Yes, the `ServicesByCategoryView` (URL `/services/category/<category>/`) displays services for a specific category.

> Does a service have its own page, where its information gets displayed (name, description, field, price per hour and date it was created) along with the name of the company which created it?

Yes, the `ServiceDetailView` (URL `/services/<pk>/`) displays all this information.

### Customer Profile & Service Request
> Logout from the Company profile and after registering and being logged in with a Customer account, navigate to the profile page. Is all his or her information available (apart from the password)?

Yes, the profile page displays username, email, and date of birth.

> Go to the previous created service and request it with a 2 hours interval. Were you asked for an address and a service time (in hours)?

Yes, the `RequestServiceView` uses `ServiceRequestForm` which asks for address and service hours.

> Go to the user (Customer) profile. Does the service requested before, appears in the customer page as a previously requested service?

Yes, the profile page lists all requested services.

> Does the service requested appear with the price of 21.00 (2 hours * 10.50)?

Yes, the cost is calculated and displayed.

> Is there a page showing the most requested services from the whole website?

Yes, the `MostRequestedServicesView` (URL `/services/most_requested/`) displays services ordered by request count.

### Advanced Logic
> Logout and register a new All in One Company and navigate to the service creation page. Can you choose between all of the types of service for this new service?

Yes, the logic in `ServiceForm` allows "All in One" companies to select any field, while restricting other companies to their specific field.

> Create a new Painting service. Logout from the Company and login with a Customer. Request two times that same service and go to the most requested services page. Is the list of most requested services updated with this new service?

Yes, the `MostRequestedServicesView` aggregates request counts and orders by them.

## Basic
> Does the code obey the good practices?

Yes, the code follows Django best practices:
- Uses Class-Based Views (CBVs) for standard behavior.
- Uses ModelForms for validation and HTML generation.
- Uses strict database models with relationships.
- Uses templates with inheritance.
- Logic is encapsulated in forms and models where appropriate.

## Bonus
> Is a system implemented where Customers can rate the services they have requested?

No, this bonus was not implemented.

> Is there a page system in the service list page?

Yes, `ServiceListView` has `paginate_by = 10` and the template includes pagination controls.

> Are there any other bonuses implemented?

Added navigation links for categories in service lists and details.

> Did the student implement its own display and design?

Used a basic CSS file provided, with some structural improvements in templates (like service cards).

## Social
> Did you learn anything from this project?

Yes, learned about Django's authentication system, OneToOne fields, form validation, and complex querying with `annotate`.

> Would you recommend/nominate this program as an example for the rest of the school?

Yes, it's a solid foundation for a service marketplace.
