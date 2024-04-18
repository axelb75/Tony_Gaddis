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


def main():
    item_list = []
    number = int(input('Сколько будет товаров? '))

    for i in range(number):
        print(f'Введите данные {i + 1}-го товара:')
        input_info(item_list)
        print()

    print('Наличие товаров:')
    for good in item_list:
        print(f'\tТовар №{item_list.index(good) + 1}:')
        output_info(good)


def input_info(item_list):
    item = input('Описание товара: ')
    quantity = int(input('Количество на складе: '))
    price = float(input('Цена: '))
    retail_item = RetailItem(item, quantity, price)
    item_list.append(retail_item)
    

def output_info(retail_item):
    print(retail_item)
    print()

main()