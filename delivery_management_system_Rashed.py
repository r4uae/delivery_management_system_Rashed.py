from datetime import date

class Customer:
    def __init__(self, customer_id, name, email, contact, address):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._contact = contact
        self._address = address
    
    def get_customer_id(self):
        return self._customer_id
    
    def set_customer_id(self, customer_id):
        self._customer_id = customer_id
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    
    def get_contact(self):
        return self._contact
    
    def set_contact(self, contact):
        self._contact = contact
    
    def get_address(self):
        return self._address
    
    def set_address(self, address):
        self._address = address
    
    def get_customer_details(self):
        return f"{self._name}, {self._contact}, {self._address}"
    
    def place_order(self):
        pass  # Function to place an order

class Order:
    def __init__(self, order_id, customer, reference_no, order_date, delivery_method):
        self._order_id = order_id
        self._customer = customer
        self._reference_no = reference_no
        self._order_date = order_date
        self._delivery_method = delivery_method
        self._items = []
    
    def get_order_id(self):
        return self._order_id
    
    def set_order_id(self, order_id):
        self._order_id = order_id
    
    def get_customer(self):
        return self._customer
    
    def set_customer(self, customer):
        self._customer = customer
    
    def get_reference_no(self):
        return self._reference_no
    
    def set_reference_no(self, reference_no):
        self._reference_no = reference_no
    
    def get_order_date(self):
        return self._order_date
    
    def set_order_date(self, order_date):
        self._order_date = order_date
    
    def get_delivery_method(self):
        return self._delivery_method
    
    def set_delivery_method(self, delivery_method):
        self._delivery_method = delivery_method
    
    def add_item(self, item):
        self._items.append(item)
    
    def get_items(self):
        return self._items
    
    def calculate_total(self):
        return sum(item.total_price() for item in self._items)
    
    def generate_delivery_note(self):
        pass  # Function to generate a delivery note

class Item:
    def __init__(self, item_code, description, quantity, unit_price):
        self._item_code = item_code
        self._description = description
        self._quantity = quantity
        self._unit_price = unit_price
    
    def get_item_code(self):
        return self._item_code
    
    def set_item_code(self, item_code):
        self._item_code = item_code
    
    def get_description(self):
        return self._description
    
    def set_description(self, description):
        self._description = description
    
    def get_quantity(self):
        return self._quantity
    
    def set_quantity(self, quantity):
        self._quantity = quantity
    
    def get_unit_price(self):
        return self._unit_price
    
    def set_unit_price(self, unit_price):
        self._unit_price = unit_price
    
    def total_price(self):
        return self._quantity * self._unit_price
    
class Delivery:
    def __init__(self, delivery_id, order, courier, delivery_date, total_weight):
        self._delivery_id = delivery_id
        self._order = order
        self._courier = courier
        self._delivery_date = delivery_date
        self._total_weight = total_weight
    
    def get_delivery_id(self):
        return self._delivery_id
    
    def set_delivery_id(self, delivery_id):
        self._delivery_id = delivery_id
    
    def get_order(self):
        return self._order
    
    def set_order(self, order):
        self._order = order
    
    def get_courier(self):
        return self._courier
    
    def set_courier(self, courier):
        self._courier = courier
    
    def get_delivery_date(self):
        return self._delivery_date
    
    def set_delivery_date(self, delivery_date):
        self._delivery_date = delivery_date
    
    def get_total_weight(self):
        return self._total_weight
    
    def set_total_weight(self, total_weight):
        self._total_weight = total_weight
    
    def update_status(self):
        pass  # Function to update delivery status

class Courier:
    def __init__(self, courier_id, name, phone):
        self._courier_id = courier_id
        self._name = name
        self._phone = phone
    
    def get_courier_id(self):
        return self._courier_id
    
    def set_courier_id(self, courier_id):
        self._courier_id = courier_id
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_phone(self):
        return self._phone
    
    def set_phone(self, phone):
        self._phone = phone
    
    def update_status(self):
        pass  # Function for the courier to update delivery status

class Payment:
    def __init__(self, payment_id, order, amount, taxes, total_charges):
        self._payment_id = payment_id
        self._order = order
        self._amount = amount
        self._taxes = taxes
        self._total_charges = total_charges
    
    def get_payment_id(self):
        return self._payment_id
    
    def set_payment_id(self, payment_id):
        self._payment_id = payment_id
    
    def get_order(self):
        return self._order
    
    def set_order(self, order):
        self._order = order
    
    def get_amount(self):
        return self._amount
    
    def set_amount(self, amount):
        self._amount = amount
    
    def get_taxes(self):
        return self._taxes
    
    def set_taxes(self, taxes):
        self._taxes = taxes
    
    def get_total_charges(self):
        return self._total_charges
    
    def set_total_charges(self, total_charges):
        self._total_charges = total_charges
    
    def process_payment(self):
        pass  # Function to process payment

# Creating Customer objects
customer1 = Customer(1, "Sarah Johnson", "sarah.johnson@example.com", "+97123456789", "45 Knowledge Avenue, Dubai, UAE")
customer2 = Customer(2, "John Doe", "john.doe@example.com", "+97198765432", "12 Business Street, Dubai, UAE")

# Creating Order objects
order1 = Order("DEL123456789", customer1, "DN-2025-001", date(2025, 1, 25), "Courier")
order2 = Order("DEL987654321", customer2, "DN-2025-002", date(2025, 2, 5), "Courier")

# Adding Items
items = [
    Item("ITM001", "Wireless Keyboard", 1, 100.00),
    Item("ITM002", "Wireless Mouse & Pad Set", 1, 75.00),
    Item("ITM003", "Laptop Cooling Pad", 1, 120.00),
    Item("ITM004", "Camera Lock", 3, 15.00)
]
for item in items:
    order1.add_item(item)

# Creating Courier objects
courier1 = Courier("C001", "Fast Logistics", "+9715550001")
courier2 = Courier("C002", "Express Delivery", "+9715550002")

# Creating Delivery objects
delivery1 = Delivery("D001", order1, courier1, date(2025, 1, 25), 7)
delivery2 = Delivery("D002", order2, courier2, date(2025, 2, 5), 5)

# Creating Payment objects
payment1 = Payment("P001", order1, order1.calculate_total(), 13.50, 283.50)
payment2 = Payment("P002", order2, order2.calculate_total(), 10.00, 210.00)

# Displaying the Delivery Note
print(f"Delivery Note:\n{'-'*50}")
print(f"Recipient: {customer1.get_customer_details()}")
print(f"Order Number: {order1.get_order_id()}")
print(f"Reference Number: {order1.get_reference_no()}")
print(f"Delivery Date: {order1.get_order_date()}")
print(f"Delivery Method: {order1.get_delivery_method()}")
print(f"Total Weight: {delivery1.get_total_weight()} kg\n")
print("Items Delivered:")
for item in order1.get_items():
    print(f"{item.get_item_code()}: {item.get_description()}, Quantity: {item.get_quantity()}, Unit Price: AED {item.get_unit_price()}, Total: AED {item.total_price()}")
print("\nFinancial Information:")
print(f"Subtotal: AED {payment1.get_amount()}")
print(f"Taxes and Fees: AED {payment1.get_taxes()}")
print(f"Total Charges: AED {payment1.get_total_charges()}")
