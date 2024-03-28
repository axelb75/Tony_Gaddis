def main():
    while True:
        user_date = input('Введите дату в формате дд/мм/гггг: ')
        user_date_list = listing_user_date(user_date)
        if len(user_date_list[0]) == 2 and len(user_date_list[1]) == 2 and\
                len(user_date_list[2]) == 4:
            print(f'\nНовый формат даты: {convert_date(user_date_list)} г.')
            break
        else:
            print('\nНеверный формат даты.')


def listing_user_date(date):
    list = date.split('/')
    return list

def convert_date(date):
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
             'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    month = ''
    for i in range(1, len(months) + 1):
        if i == int(date[1]):
            month = months[i - 1]
    date[1] = month
    new_date = ' '.join(date)
    return new_date


main()