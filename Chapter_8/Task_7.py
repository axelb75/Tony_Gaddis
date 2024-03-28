def main():
    in_text = open('text.txt', 'r').read()
    up, low, digit, sp = calculate_sym(in_text)
    print(f'Количество букв в верхнем регистре: {up}'
          f'\nКоличество букв внижнем регистре: {low}'
          f'\nКоличество цифр: {digit}'
          f'\nКоличество пробелов: {sp}')

def calculate_sym(text):
    letter_up = 0
    letter_low = 0
    number = 0
    space = 0
    for symbol in text:
        if symbol.isupper():
            letter_up += 1
        elif symbol.islower():
            letter_low += 1
        elif symbol.isdigit():
            number += 1
        elif symbol.isspace():
            space += 1
    return letter_up, letter_low, number, space


main()