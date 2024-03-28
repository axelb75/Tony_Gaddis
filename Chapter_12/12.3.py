def print_stars(num, start):
    if num > 0:
        print('*' * start)
        print_stars(num - 1, start + 1)


n = int(input('Введите число строк: '))
print_stars(n, 1)