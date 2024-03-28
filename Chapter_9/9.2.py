import random

capitals = {'Адыгея': 'Майкоп','Республика Алтай': 'Горно-Алтайск', 'Башкортостан': 'Уфа', 'Бурятия': 'Улан-Удэ',
            'Дагестан': 'Махачкала', 'Ингушетия': 'Магас', 'Кабардино-Балкария': 'Нальчик', 'Калмыкия': 'Элиста',
            'Карачаево-Черкесия': 'Черкесск', 'Карелия': 'Петрозаводск', 'Республика Коми': 'Сыктывкар',
            'Марий Эл': 'Йошкар-Ола', 'Мордовия': 'Саранск', 'Якутия': 'Якутск', 'Северная Осетия': 'Владикавказ',
            'Татарстан': 'Казань', 'Тыва': 'Кызыл', 'Удмуртия': 'Ижевск', 'Хакасия': 'Абакан', 'Чечня': 'Грозный',
            'Чувашия': 'Чебоксары', 'Алтайский край': 'Барнаул', 'Забайкальский край': 'Чита',
            'Камчатский край': 'Петропавловск-Камчатский', 'Краснодарский край': 'Краснодар',
            'Красноярский край': 'Красноярск', 'Пермский край': 'Пермь', 'Приморский край': 'Владивосток',
            'Ставропольский край': 'Ставрополь', 'Хабаровский край': 'Хабаровск', 'Амурская область': 'Благовещенск',
            'Архангельская область': 'Архангельск', 'Астраханская область': 'Астрахань',
            'Белгородская область': 'Белгород', 'Брянская область': 'Брянск', 'Владимирская область': 'Владимир',
            'Волгоградская область': 'Волгоград', 'Вологодская область': 'Вологда', 'Воронежская область': 'Воронеж',
            'Ивановская область': 'Иваново', 'Иркутская область': 'Иркутск', 'Калининградская область': 'Калининград',
            'Калужская область': 'Калуга', 'Кемеровская область': 'Кемерово', 'Кировская область': 'Киров',
            'Костромская область': 'Кострома', 'Курганская область': 'Курган', 'Курская область': 'Курск',
            'Ленинградская область': 'Санкт-Петербург', 'Липецкая область': 'Липецк', 'Магаданская область': 'Магадан',
            'Московская область': 'Москва', 'Мурманская область': 'Мурманск', 'Нижегородская область': 'Нижний Новгород',
            'Новгородская область': 'Великий Новгород', 'Новосибирская область': 'Новосибирск', 'Омская область': 'Омск',
            'Оренбургская область': 'Оренбург', 'Орловская область': 'Орёл', 'Пензенская область': 'Пенза',
            'Псковская область': 'Псков', 'Ростовская область': 'Ростов-на-Дону', 'Рязанская область': 'Рязань',
            'Самарская область': 'Самара', 'Саратовская область': 'Саратов', 'Сахалинская область': 'Южно-Сахалинск',
            'Свердловская область': 'Екатеринбург', 'Смоленская область': 'Смоленск', 'Тамбовская область': 'Тамбов',
            'Тверская область': 'Тверь', 'Томская область': 'Томск', 'Тульская область': 'Тула',
            'Тюменская область': 'Тюмень', 'Ульяновская область': 'Ульяновск', 'Челябинская область': 'Челябинск',
            'Ярославская область': 'Ярославль', 'Еврейская автономная область': 'Биробиджан',
            'Ненецкий автономный округ': 'Нарьян-Мар', 'Ханты-Мансийский автономный округ — Югра': 'Ханты-Мансийск',
            'Чукотский автономный округ': 'Анадырь', 'Ямало-Ненецкий автономный округ': 'Салехард'}

print('Поугадываешь столицы регионов нашей Родины?\nУ тебя 10 попыток. Начнём:')
count = 0
for i in range(10):
    district = random.choice(list(capitals.keys()))
    print('\nПопытка', i + 1,'\nРегион России:', district, '\nВведи столицу региона: ', end='')
    capital = input('')
    if capital == capitals[district]:
        print('Отлично, ты знаешь свою страну.')
        count += 1
    else:
        print('Двойка тебе по географии.\nПравильный ответ:', capitals[district])
    del(capitals[district ])

print('\nТы угадал', count, 'столиц.')