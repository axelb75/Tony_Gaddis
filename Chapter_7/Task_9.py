population = open('USPopulation.txt', 'r').readlines()
for i in range(len(population)):
    population[i] = int(population[i].rstrip('\n'))

max_change = 0
max_year = 0
min_change = population[1] - population[0]
min_year = 0
average_change_population = (population[len(population) - 1] - population[0]) / len(population)
average_population = sum(population) / len(population)
for i in range(len(population) - 2):
    change_population = population[i + 1] - population[i]
    if change_population > max_change:
        max_change = change_population
        max_year = i + 1951
    elif change_population < min_change:
        min_change = change_population
        min_year = i + 1951

print(f'Среднегодовое изменение численности: {average_change_population:.2f} тысяч человек.'
      f'\nСреднегодовая численность населения: {average_population:.2f} тысяч человек.'
      f'\nМаксимальное увеличение численности {max_change} тысяч человек в {max_year} году.'
      f'\nМинимальное увеличение численности {min_change} тысяч человек в {min_year} году.')