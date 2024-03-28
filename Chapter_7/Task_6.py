def main():
    num_list = []
    N = int(input('Длина списка: '))

    for i in range(N):
        num = int(input(f"Введите {i + 1} число списка: "))
        num_list.append(num)

    print('Исходный список:', num_list)
    sort_list(num_list)

def sort_list(list):
    n = int(input('Введите число для проверки: '))
    index = 0
    while index < len(list):
        if list[index] < n:
            list.remove(list[index])
        else:
            index += 1
    print('Изменённый список:', list)


main()