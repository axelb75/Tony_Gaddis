def main():
    number = str(input('Введите ряд цифр: '))
    print('Сумма цифр:', calculate_sum(number))


def calculate_sum(num):
    sum = 0
    for sym in num:
        sum += int(sym)
    return sum


main()