def main():
    full_name = input('Введите ФИО: ')
    print('Инициалы:', generate_fio(full_name))


def generate_fio(name):
    fio = name[0] + '.'
    index = 0
    for sym in name:
        if sym == ' ':
            fio += name[index + 1] + '.'
        index += 1
    return fio


main()