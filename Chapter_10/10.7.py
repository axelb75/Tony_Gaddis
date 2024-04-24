import pickle
import Employee

filename = 'Contacts.bin'

def main():
    my_contacts = load_contacts()

    choise = 0
    while choise != 5:
        choise = menu_choise()

        if choise == 1:
            search_contact(my_contacts)
        elif choise == 2:
            add_contact(my_contacts)
        elif choise == 3:
            change_contact(my_contacts)
        elif choise == 4:
            delete_contact(my_contacts)
    
    save_contacts(my_contacts)


def load_contacts():
    try:
        input_file = open(filename, 'rb')
        contact_dict = pickle.load(input_file)
        input_file.close()
    except FileNotFoundError:
        contact_dict = {}

    return contact_dict


def menu_choise():
    print('\nМеню\n' + '-' * 20)
    print('1. Найти контакт\n'
          '2. Добавить контакт\n'
          '3. Редактировать существующий контакт\n'
          '4. Удалить существующий контакт\n'
          '5. Выход из программы')
    print()
    choise = int(input('Введите пункт меню: '))

    while choise < 1 or choise > 5:
        choise = int(input('Некорректные данные.\nПовторите ввод: '))

    print('-' * 20)
    return choise


def search_contact(contacts):
    id = int(input('Введите ID-номер для поиска: '))
    print()
    if id in contacts:
        print(contacts[id])
    else:
        print('Контакт не найден.')
    print('-' * 20)


def add_contact(contacts):
    name = input('Введите имя: ')
    id = int(input('Введите ID: '))
    dept = input('Введите отдел: ')
    post = input('Введите должность: ')
    contact = Employee.Employee(name, id, dept, post)

    if contact not in contacts:
        contacts[id] = contact
        print('\nЗапись добавлена')
    else:
        print('Такая запись уже существует.')
    print('-' * 20)


def change_contact(contacts):
    id = int(input('Введите ID-номер для редактирования контакта: '))
    if id in contacts:
        name = input('Введите имя: ')
        dept = input('Введите отдел: ')
        post = input('Введите должность: ')
        contact = Employee.Employee(name, id, dept, post)
        contacts[id] = contact
        print('\nДанные контакта изменены.')
    else:
        print('Контакт не найден.')
    print('-' * 20)


def delete_contact(contacts):
    id = int(input('Введите ID-номер для поиска и удаления контакта: '))
    if id in contacts:
        del contacts[id]
        print('\nКонтакт удалён.')
    else:
        print('Контакт не найден.')
    print('-' * 20)


def save_contacts(contacts):
    output_file = open(filename, 'wb')
    pickle.dump(contacts, output_file)
    output_file.close()
    
    
if __name__ == '__main__':
    main()