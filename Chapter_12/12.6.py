def summa_num(num):
    if num > 0:
        return num + summa_num(num - 1)
    else:
        return 0


number = int(input('Введите число: '))
print(f'Сумма чисел от 1 до {number}: {summa_num(number)}')