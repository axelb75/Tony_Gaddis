def exponentiation(num, deg):
    if deg == 0:
        return 1
    else:
        return num * exponentiation(num, deg - 1)

number = int(input('Введите число: '))
degree = int(input('Введите степень: '))

print('Число {} в степени {}: {}'.format(number, degree, exponentiation(number, degree)))