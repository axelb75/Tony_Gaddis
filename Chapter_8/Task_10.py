alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л',
            'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш',
            'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
text_in = input('Введите текст: ')
text_in = text_in.upper()
max_sym = 0
index = 0
for i in range(len(alphabet)):
    total_sym = text_in.count(alphabet[i])
    if total_sym > max_sym:
        max_sym = total_sym
        index = i

print('\nСамый частый символ:', alphabet[index], '\nКоличество повторений:', max_sym)