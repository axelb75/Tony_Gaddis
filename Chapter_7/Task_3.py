print('Задание 3. Статистика дождевых осадков')

rainfall = []
total_rainfall = 0

for i in range(12):
    month_rainfall = float(input(f'Введите кол-во осадков за {i + 1} месяц: '))
    rainfall.append(month_rainfall)

for month in rainfall:
    total_rainfall += month

average_rainfall = total_rainfall / len(rainfall)
max_month = max(rainfall)
min_month = min(rainfall)
index_max_rainfall = rainfall.index(max_month)
index_min_rainfall = rainfall.index(min_month)

print('-' * 20, '\nСуммарное кол-во осадков за год:', round(total_rainfall, 1),
      '\nСреднемесячное кол-во осадков:', round(average_rainfall, 1), '\n',
      '\nМесяц с максимальным уровнем осадков:', index_max_rainfall + 1,
      '\nКол-во осадков в', index_max_rainfall + 1, 'месяце:', max_month, '\n',
      '\nМесяц с минимальным уровнем осадков:', index_min_rainfall + 1,
      '\nКол-во осадков в', index_min_rainfall + 1, 'месяце:', min_month)

print('-' * 20)