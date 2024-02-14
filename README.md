# PolicyManagement_system
An insurance company wants to create a policy management system to manage policyholders, products, and payments.
Classes
1. **PolicyHolder (policyholder.py)**
This class represents a policyholder and includes the following methods:
__init__(self, id, name, status='Active'): Constructor to initialize a policyholder with a unique ID, name, and default status as 'Active'.
suspend(self): Method to suspend a policyholder.
reactivate(self): Method to reactivate a suspended policyholder.
display_details(self): Method to display the policyholder's details, including ID, name, status, and associated products.

2. **Product (product.py)**
This class represents an insurance product and includes the following methods:
__init__(self, code, name, price): Constructor to initialize a product with a unique code, name, and price.
update_price(self, new_price): Method to update the price of a product.
suspend(self): Method to suspend a product.
display_details(self): Method to display the product details, including code, name, price, and status.

**3. Payment (payment.py)**
This class represents a payment transaction and includes the following methods:
__init__(self, policyholder, amount, date): Constructor to initialize a payment with a reference to the policyholder, payment amount, and date.
process_payment(self): Method to simulate processing a payment.
send_payment_reminder(self): Method to simulate sending a payment reminder.
apply_penalty(self): Method to simulate applying a penalty for overdue payment.

**Policyholder Demonstration (main.py)**
This script demonstrates the usage of the implemented classes by creating instances of policyholders, products, and payments. It showcases the basic functionalities of registering, suspending, reactivating policyholders, managing products, and processing payments.
