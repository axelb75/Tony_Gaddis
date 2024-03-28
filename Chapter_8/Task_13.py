def main():
    contents = open('pbnumbers.txt', 'r').readlines()
    for index in range(len(contents)):
        contents[index] = contents[index].rstrip('\n')

    master_list = unified_list(contents)
    numbersfound, timesfound = times_each_appears(master_list)

    top10common(timesfound, numbersfound)
    bottom10common(timesfound, numbersfound)
#    top10overdue(timesfound, numbersfound, master_list)
#    seperate_frequency(contents)


def unified_list(number_list):
    master_list = []
    for num in number_list:
        num_list = num.split()
        master_list += num_list
    return master_list


def times_each_appears(a_list):
    counter = 1
    numbersfound = []
    timesfound = []

    for number in a_list:
        if number not in numbersfound:
            numbersfound.append(number)
            timesfound.append(counter)
        else:
            i = numbersfound.index(number)
            timesfound[i] += 1

    return numbersfound, timesfound


def top10common(times, numbers):
    top10times = []
    top10numbers = []
    for i in range(10):
        index = (times.index(max(times)))
        top10numbers.append(numbers[index])
        top10times.append(times[index])
        del numbers[index]
        del times[index]
    print('\nСамые распространённые числа')
    print('Число\tКол-во повторов')
    print('-----\t---------------')
    for index in range(len(top10numbers)):
        print(top10numbers[index], '\t --->\t', top10times[index])


def bottom10common(times, numbers):
    bottom10times = []
    bottom10numbers = []
    for i in range(10):
        index = times.index(min(times))
        bottom10numbers.append(numbers[index])
        bottom10times.append(times[index])
        del numbers[index]
        del times[index]
    print('\nСамые НЕраспространённые числа')
    print('Число\tКол-во повторов')
    print('-----\t---------------')
    for index in range(len(bottom10numbers)):
        print(bottom10numbers[index], '\t --->\t', (bottom10times[index]))





main()