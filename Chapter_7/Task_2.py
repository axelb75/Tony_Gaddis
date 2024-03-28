print('Задание 2. Генератор лотерейных чисел')

import random
lottery_number = []

while len(lottery_number) < 7:
    number = random.randint(0, 9)
    if number in lottery_number:
        number = random.randint(0, 9)
    else:
        lottery_number.append(number)

print('Выигрышная комбинация чисел:', lottery_number)

print('-' * 20)