def print_num(n):
    if n != 1:
        print_num(n-1)
    print(n, end=' ')


num = int(input('Введите число: '))
print_num(num)