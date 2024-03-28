def check_names():
    if user_boy_name in boy_names:
        print('Данное имя находится среди популярных имён мальчиков.')
    else:
        print('Данного имени нет среди популярных имён мальчиков.')
    if user_girl_name in girl_names:
        print('Данное имя находится среди популярных имён девочек.')
    else:
        print('Данного имени нет среди популярных имён девочек.')


boy_names = open('BoyNames.txt', 'r').read().splitlines()
girl_names = open('GirlNames.txt', 'r').read().splitlines()

user_boy_name = input('Введите имя мальчика: ')
user_girl_name = input('Введите имя девочки: ')

check_names()
