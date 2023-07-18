from item import Item

class Order():

    items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def total_price(self):
        return sum([item.quantity * item.price for item in self.items])

