print('\nЗадача 11. Математический тест')
#import random

#number1 = random.randint(0, 999)
#number2 = random.randint(0, 999)

#print(' ', number1, '\n+', number2)


#def calc_sum(num1, num2):
#    sum = num1 + num2
#    return sum


#true_sum = calc_sum(number1, number2)
#user_sum = int(input('\nВведите результат: '))

#while user_sum != true_sum:
#    user_sum = int(input('Ошибочка. Попробуйте ещё раз: '))
#else:
#    print('\nПоздравляю! Ваш ответ правильный.')

print('-' * 20)


print('\nЗадание 12. Максимальное из двух значений')

#def calc_max_number(num_1, num_2):
#    if num_1 > num_2:
#        max_num = num_1
#        print('-' * 20, '\nМаксимальное из двух чисел:', max_num)
#    elif num_1 < num_2:
#        max_num = num_2
#        print('-' * 20, '\nМаксимальное из двух чисел:', max_num)
#    else:
#        print('-' * 20, '\nЧисла равны.')


#number_1 = int(input('Введите первое число: '))
#number_2 = int(input('Введите второе число: '))

#calc_max_number(number_1, number_2)

print('-' * 20)


print('\nЗадание 13. Высота падения')

#def calc_falling_distance(time):
#    distance = 9.8 * time**2 / 2
#    return distance


#time = int(input('\nВвдите время падения: '))
#print('-' * 20)
#for falling_time in range(1, time + 1):
#    falling_distance = calc_falling_distance(falling_time)
#    print('Время падения:', falling_time, 'сек.\tРасстояние:',
#          round(falling_distance, 2), 'м.')

print('-' * 20)


print('\nЗадание 14. Кинетическая энергия')


#def calc_kinetic_energy(weight, speed):
#    kinetic_energy = weight * speed**2 / 2
#    return kinetic_energy


#user_weight = float(input('Введите массу тела в килограммах: '))
#user_speed = float(input('Введите скорость в метрах в секунду: '))

#energy = calc_kinetic_energy(user_weight, user_speed)

#print()
#print('Кинетическая энергия тела:', round(energy, 3), 'Дж.')
print('-' * 20)


print('\nЗадание 15. Средний балл и его уровень')

#def main():
#   grade_sum = 0
#    for i in range(1, 6):
#        print()
#        grade = int(input(f'Введите {i} оценку (от 0 до 100): '))

#        grade_sum += grade

#        average = calc_average(grade_sum)
#        determine = calc_determine_grade(grade)
#        print('Буквенный уровень:', determine)
#    print('-' * 20, '\nСредний балл:', average)


#def calc_average(grade_summa):
#    average_grade = grade_summa / 5
#    return average_grade


#def calc_determine_grade(user_grade):
#    if user_grade >= 90:
#        determine_grade = 'A'
#    elif 80 <= user_grade < 90:
#        determine_grade = 'B'
#    elif 70 <= user_grade < 80:
#        determine_grade = 'C'
#    elif 60 <= user_grade < 70:
#        determine_grade = 'D'
#    elif user_grade < 60:
#        determine_grade = 'E'
#    return determine_grade


#main()

print('-' * 20)


print('\nЗадача 16. Счётчик чётных/нечётных чисел')

#import random

#number_even = 0
#number_odd = 0

#for i in range(1,101):
#    number = random.randint(0, 9999)
#    if number % 2 == 0:
#        number_even += 1
#    else:
#        number_odd += 1

#print('Чётных чисед:', number_even, '\nНечётных чисел:', number_odd)

print('-' * 20)


print('\nЗадача 17. Простые числа')

#def is_prime(num):
#    count = 0
#    for i in range(2, num):
#        if num % i == 0:
#            count += 1
#    if count > 0:
#        status = False
#    else:
#        status = True
#    return status


#number = int(input('Введите число: '))
#if is_prime(number):
#    print('Это число простое')
#else:
#    print('Это число не является простым')

print('-' * 20)


print('\nЗадача 18. Список простых чисел')

#for number in range(1, 101):
#    if is_prime(number):
#        print(number, end = '\t')

print('-' * 20)


print('\nЗадача 19. Будущая стоимость')

#def calc_sum_future(sum_p, rate, month):
#    sum_future = sum_p * (1 + rate / 1200)**month
#    return sum_future


#sum_present = float(input('Введите текущую сумму на счёте: '))
#interest_rate = float(input('Введите годовую процентную ставку: '))
#months = int(input('Введите количество месяцев: '))

#print('-' * 20)
#print('Будущая сумма на счёте:',
#      round(calc_sum_future(sum_present, interest_rate, months), 2))

print('-' * 20)


print('\nЗадача 20. Игра в угадывание случайного числа')

import random

def main():
    number_pc = random.randint(1,100)
    print('-' * 20)
    number_user = int(input('Угадай число от 1 до 100: '))
    count = 1
    if number_user != 0:
        guess_number(number_pc, number_user,count)


def guess_number(num_pc, num_user, count):
    while True:
        if num_user == num_pc:
            print('-' * 20, '\nПоздравляю! Ты угадал с', count, 'попытки.')
            main()
            break
        elif num_user > num_pc:
            num_user = int(input('Слишком много, попробуйте ещё раз: '))
        else:
            num_user = int(input('Слишком мало, попробуйте ещё раз: '))
        count += 1

main()

print('-' * 20)


print('\nЗадача 21. Игра "Камень, ножницы, бумага"')

import random

def main():
    thing_pc = random.randint(1, 3)
    question = str(input('Выбери камень, ножницы или бумагу: '))
    while True:
        if question == 'Камень' or question == 'камень':
            thing_user = 1
            break
        elif question == 'Ножницы' or question == 'ножницы' :
            thing_user = 2
            break
        elif question == 'Бумага' or question == 'бумага':
            thing_user = 3
            break
        else:
            print('-' * 20, '\nНеправильно.')
            question = input('Повтори выбор камня, ножниц или бумаги: ')

    if thing_pc == 1:
        print('-' * 20, '\nВыбор комьютера: Камень')
    elif thing_pc == 2:
        print('-' * 20, '\nВыбор комьютера: Ножницы')
    elif thing_pc == 3:
        print('-' * 20, '\nВыбор комьютера: Бумага')

    compare_values(thing_pc, thing_user)


def compare_values(value_pc, value_user):
    if value_pc == 1 and value_user == 2:
        print('-' * 20, '\nПобедил компьютер. Камень разбивает ножницы.')
    elif value_pc == 1 and value_user == 3:
        print('-' * 20, '\nПоздравляю! Ты победил. Бумага заворачивает камень.')
    elif value_pc == 2 and value_user == 1:
        print('-' * 20, '\nПоздравляю! Ты победил. Камень разбивает ножницы.')
    elif value_pc == 2 and value_user == 3:
        print('-' * 20, '\nПобедил компьютер. Ножницы режут бумагу.')
    elif value_pc == 3 and value_user == 1:
        print('-' * 20, '\nПобедил компьютер. Бумага заворачивает камень.')
    elif value_pc == 3 and value_user == 2:
        print('-' * 20, '\nПоздравляю! Ты победил. Ножницы режут бумагу.')
    else:
        print('-' * 20, '\nНичья.')
    print('-' * 20)
    cont = int(input('Сыграем ещё раз? (Да - 1, Нет - любая клавиша): '))
    if cont == 1:
        main()


main()