print('Задание 4. Программа анализа чисел')

twenty_numbers = []
sum_numbers = 0

for i in range(20):
    number = int(input(f'Введите {i + 1} число: '))
    twenty_numbers.append(number)

for num in twenty_numbers:
    sum_numbers += num

max_number = max(twenty_numbers)
min_number = min(twenty_numbers)
average_number = sum_numbers / len(twenty_numbers)

print('-' * 20, '\nСписок чисел:', twenty_numbers,
      '\nНаибольшее число в списке:', max_number,
      '\nНаименьшее число в списке:', min_number,
      '\nСумма чисел в списке:', sum_numbers,
      '\nСреднее арифметическое чисел в списке:', average_number)