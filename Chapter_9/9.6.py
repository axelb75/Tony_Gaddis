def input_text():
    in_file_1 = open('Text_9.6.1.txt', 'r')
    text_1 = in_file_1.read()
    text_1 = text_1.replace('.', '')
    text_1 = text_1.replace(',', '')
    text_1 = text_1.replace('?', '')
    text_1 = text_1.replace('!', '')
    text_1 = text_1.replace(';', '')
    text_1 = text_1.replace(':', '')
    text_1 = text_1.replace('-', '')
    text_list_1 = text_1.split(' ')
    in_file_1.close()

    in_file_2 = open('Text_9.6.2.txt', 'r')
    text_2 = in_file_2.read()
    text_2 = text_2.replace('.', '')
    text_2 = text_2.replace(',', '')
    text_2 = text_2.replace('?', '')
    text_2 = text_2.replace('!', '')
    text_2 = text_2.replace(';', '')
    text_2 = text_2.replace(':', '')
    text_2 = text_2.replace('-', '')
    text_list_2 = text_2.split(' ')
    in_file_2.close()

    return text_list_1, text_list_2


def main():
    text_1, text_2 = input_text()
#    text_1 = input('Текст 1: ').split(' ')
#    text_2 = input('Текст 2: ').split(' ')
    text_1 = set(text_1)
    text_2 = set(text_2)

    print('\nСписок всех уникальных слов:', sorted(text_1 | text_2))
    print('\nСписок слов, входящих в оба текста:', sorted(text_1 & text_2))
    print('\nСписок слов, входящих в первый и не входящих во второй:', sorted(text_1 - text_2))
    print('\nСписок слов, входящих во второй и не входящих в первый:', sorted(text_2 - text_1))
    print('\nСписок слов, входящих в первый  или во второй, но не входящих в оба одновременно:', sorted(text_1 - text_2) + sorted(text_2 - text_1))


main()