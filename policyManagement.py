#create a class for policyHolder management to implement register, suspend and reactivate

class PolicyHolder:
    def __init__(self, id, name, status='Active'):
        self.id = id
        self.name = name
        self.status = status
        self.products = []

    def suspend(self):
        self.status = 'Suspended'

    def reactivate(self):
        self.status = 'Active'

    def display_details(self):
        print(f"Policyholder ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Status: {self.status}")
        print("Products:")
        for product in self.products:
            print(f" - {product}")

#create a class for product management to create, update, removing or suspending product

class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.status = 'Active'

    def update_price(self, new_price):
        self.price = new_price

    def suspend(self):
        self.status = 'Suspended'

    def display_details(self):
        print(f"Product Code: {self.code}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Status: {self.status}")

#create a class for payment processes, reminders and penalties

class Payment:
    def __init__(self, policyholder, amount, date):
        self.policyholder = policyholder
        self.amount = amount
        self.date = date

    def process_payment(self):
        # Implement payment processing logic
        print(f"Payment of ${self.amount} processed for {self.policyholder.name} on {self.date}")

    def send_payment_reminder(self):
        # Implement reminder logic
        print(f"Reminder: Payment of ${self.amount} due for {self.policyholder.name}")

    def apply_penalty(self):
        # Implement penalty logic
        print(f"Penalty applied: Payment for {self.policyholder.name} is overdue")

from policyholder import PolicyHolder
from product import Product
from payment import Payment

# Create products
product1 = Product("P001", "Product A", 100)
product2 = Product("P002", "Product B", 150)

# Create policyholders
policyholder1 = PolicyHolder(1, "John Doe")
policyholder2 = PolicyHolder(2, "Jane Smith")

# Add products to policyholders
policyholder1.products.append(product1.name)
policyholder2.products.append(product2.name)

# Display account details
policyholder1.display_details()
policyholder2.display_details()

# Process payments
payment1 = Payment(policyholder1, 100, "2024-02-10")
payment2 = Payment(policyholder2, 150, "2024-02-09")

payment1.process_payment()
payment2.send_payment_reminder()
payment2.apply_penalty()
