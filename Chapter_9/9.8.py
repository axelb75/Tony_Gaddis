def main():
#    in_file = open('EmailBook.txt', 'w+')
#   email_book  = in_file.read()
    email_book = {}
    print('\nОсновное меню:\n1 - Поиск контакта\n2 - Добавление нового контакта\n3 - Редактирование существующего контакта\n4 - Удаление существующего контакта\n5 - Выход')
    main_menu = int(input('Введите пункт меню: '))
    while True:
        status = False
        if main_menu == 1:
            print('Поиск')
            search_contact(email_book)
        elif main_menu == 2:
            print('Новый')
            add_new_contact(email_book)
            status = True
        elif main_menu == 3:
            print('Редактирование')
            change_contact(email_book)
            break
        elif main_menu == 4:
            print('Удаление')
            delete_contact(email_book)
            break
        elif main_menu == 5:
            break
        else:
            print('Некорректный ввод.')
            main_menu = int(input('Введите пункт меню: '))
        

def search_contact(book):
    name = input('Введите имя: ')
    if name in book:
        print('Почта:', book[name])
    else:
        print('Контакт отсутствует')


def add_new_contact(book):
    name = input('Введите имя: ')
    if name not in book:
        book[name] = input('Введите e-mail: ')
    else:
        print('Контакт уже существует')
    return book


def change_contact(book):
    name = input('Введите имя: ')
    if name in book:
        name = input('Введите новое имя: ')
        email = input('Введите новый e-mail: ')
        book[name] = email
    else:
        print('Контакт отсутствует')
    print(book)
    return book


#def delete_contact():
    


#    in_file.write(email_book)
#    in_file.close()



main()