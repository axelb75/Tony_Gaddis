def multiply_nums(x, y):
    mult = 0
    if y != 0:
        return (x + multiply_nums(x, y - 1))
    else:
        return 0


num_1 = int(input('Первое число: '))
num_2 = int(input('Второе число: '))
print(multiply_nums(num_1, num_2))