from person import Person
from order import Order
from item import Item


class Customer(Person):

    orders = []

    def __init__(self, name, family_name, postal_code):
        self.postal_code = postal_code
        super().__init__(name, family_name)

    def create_order(self, order):
        self.orders.append(order)
