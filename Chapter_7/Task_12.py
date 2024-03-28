def main():
    while True:
        number = int(input('Введите число больше 1: '))
        if number <= 1:
            print('Число вне диапазона. Повторите ввод.')
        else:
            break

    num_list = generate_list(number)
    prime_num_list = check_list(num_list)
    output_list(prime_num_list)


def generate_list(num):
    num_list = []
    for i in range(1, num + 1):
        num_list.append(i)
    return num_list


def check_list(list):
    new_list = []
    count = 0
    for num in list:
        for i in range(2, num):
            if num % i == 0:
                count += 1
                break
        if count == 0:
            new_list.append(num)
        count = 0

    return new_list


def output_list(list):
    print('Список простых чисел:', end=' ')
    for num in list:
        print(num, end=' ')


main()