def main():
    vowel = ['А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
    consonant = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М',
             'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
    text_in = input('Введите текст: ')
    text_in = text_in.upper()
    total_vowel = calc_vowel(text_in, vowel)
    total_consonant = calc_consonant(text_in, consonant)
    print('Гласных букв в тексте:', total_vowel)
    print('Согласных букв в тексте:', total_consonant)


def calc_vowel(text, a):
    count = 0
    for sym in text:
        if sym in a:
            count += 1
    return count


def calc_consonant(text, b):
    count = 0
    for sym in text:
        if sym in b:
            count += 1
    return count


if __name__ == '__main__':
    main()