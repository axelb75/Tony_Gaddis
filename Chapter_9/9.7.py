def main():
    in_file = open('WorldSeriesWinners.txt', 'r')
    world_series_winners = in_file.read().splitlines()
    in_file.close()

    quantity_win = calc_winners_quantity(world_series_winners)
    years_win = calc_year_winners(world_series_winners)

    year_win = int(input('\nВведите год в диапазоне от 1903 до 2009: '))
    print('\nПобедитель в', year_win, 'году:', years_win[year_win])
    if years_win[year_win] == 'World Series Not Played':
        print('\nКоличество лет, когда игры не проводились, за весь период с 1903 по 2009 год:',
              quantity_win['World Series Not Played'])
    else:
        print('\nКоличество побед у этого победителя за весь период с 1903 по 2009 год:',
              quantity_win[years_win[year_win]])


def calc_winners_quantity(winners):
    winners_quantity = {}
    for winner in winners:
        if winner != 'World Series Not Played':
            winners_quantity[winner] = winners_quantity.get(winner, 0) + 1
        else:
            winners_quantity['World Series Not Played'] = winners_quantity.get('World Series Not Played', 0) + 1
    return winners_quantity


def calc_year_winners(winners):
    year_winners = {}
    for i in range(len(winners)):
        year_winners[i + 1903] = winners[i]
    return year_winners


main()