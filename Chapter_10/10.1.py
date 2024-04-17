class Pet_1:
    def __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = 0

    def set_name(self):
        self.__name = input('Кличка животного: ')

    def set_animal_type(self):
        self.__animal_type = input('Тип домашнего животного (например "собака", "кошка" или "птица"): ')

    def set_age(self):
        self.__age = int(input('Возраст животного: '))

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


my_pet_1 = Pet_1()
my_pet_1.set_name()
my_pet_1.set_animal_type()
my_pet_1.set_age()
print('\nВаше животное:\n{} по кличке {}, возраст {} лет'.
      format(my_pet_1.get_animal_type(), my_pet_1.get_name(), my_pet_1.get_age()))


class Pet_2:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


my_pet_2 = Pet_2('Jack', 'Dog', 4)

print('\nВаше животное:\n{} по кличке {}, возраст {} лет'.
      format(my_pet_2.get_animal_type(), my_pet_2.get_name(), my_pet_2.get_age()))