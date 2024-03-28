def main():
    code_sym = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    code_num = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]

    while True:
        phone_input = input('Введите номер телефона в формате ХХХ-ХХХ-ХХХХ: ')
        phone_input = phone_input.upper()
        if len(phone_input) != 12 or phone_input.count('-') != 2:
            print('Ошибка ввода.')
        else:
            break
    phone = []
    for i in range(len(phone_input)):
        if phone_input[i].isalpha():
            phone.append(str(code_num[code_sym.index(phone_input[i])]))
        else:
            phone.append(phone_input[i])
    print('Числовой формат номера:', ''.join(phone))


main()