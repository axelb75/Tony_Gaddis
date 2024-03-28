winners = open('WorldSeriesWinners.txt', 'r').read().splitlines()

command = input('Введите название команды: ')
count = 0
for i in range(len(winners)):
    if winners[i] == command:
        count += 1
print(f'Команда {command} побеждала {count} раз в Мировой серии.')