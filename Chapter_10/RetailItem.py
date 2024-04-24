class RetailItem:
    def __init__(self, item, quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price

    def set_item(self, item):
        self.item = item

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_price(self, price):
        self.price = price

    def get_item(self):
        return self.item

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    def __str__(self):
        return f'\t\tОписание: {self.item}\n\t\tКоличество на складе: {self.quantity}' \
               f'\n\t\tЦена: {self.price}'