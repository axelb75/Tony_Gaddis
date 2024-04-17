class Person:
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone


def main():
    person_list = []
    input_info(person_list)
    print('-' * 20)
    view_info(person_list)


def input_info(family_list):
    num = int(input('Сколько членов семьи? '))
    print()
    for i in range(1, num + 1):
        name = input(f'Имя {i}-го члена семьи: ')
        address = input(f'Адрес {i}-го члена семьи: ')
        age = int(input(f'Возраст {i}-го члена семьи: '))
        phone = input(f'Телефон {i}-го члена семьи: ')
        print()
        person = Person(name, address, age, phone)
        family_list.append(person)
    return family_list


def view_info(family_list):
    print('Наша семья:')
    for person in family_list:
        print('Имя: {}\tАдрес: {}\tВозраст: {}\tТелефон: {}'.
              format(person.name, person.address, person.age, person.phone))


main()