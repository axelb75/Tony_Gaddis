print('Задание 1. Общий объём продаж')

week = []
sum_profit = 0

for day in range(7):
    profit = float(input(f'Введите сумму продаж за {day + 1} день: '))
    week.append(profit)

for day in week:
    sum_profit += day

print('Продажи по дням недели:', week, '\nОбщая сумма продаж:', sum_profit)

print('-' * 20)