def main():
    matrix1 = []
    index1 = 0
    while index1 < 9:
        num = int(input(f'Введите {index1 + 1} число: '))
        if 1 <= num <= 9 and num not in matrix1:
            matrix1.append(num)
            index1 += 1
        else:
            print('Число выходит за диапазон')

    matrix2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    index2 = 0
    for i in range(3):
        for j in range(3):
            matrix2[i][j] = matrix1[index2]
            index2 += 1

    sum_list = calc_sum(matrix2)
    calc_lo_shu(sum_list)


def calc_sum(matrix):
    col_1, col_2, col_3 = 0, 0, 0
    diag_1, diag_2 = 0, 0
    sum_list = []

    for i in range(3):
        col_1 += matrix[i][0]
        col_2 += matrix[i][1]
        col_3 += matrix[i][2]
        diag_1 += matrix[i][i]
        diag_2 += matrix[i][2 - i]
    sum_list.extend([sum(matrix[0]), sum(matrix[1]), sum(matrix[2]),
                     col_1, col_2, col_3,
                     diag_1, diag_2])

    return sum_list


def calc_lo_shu(list):
    lo_shu = True
    for i in range(len(list) - 1):
        if list[i] != list[i+1]:
            print('Список не является квадратом Ло Шу.')
            break
        else:
            lo_shu = False

    if lo_shu == False:
        print('Список является квадратом Ло Шу.')


main()