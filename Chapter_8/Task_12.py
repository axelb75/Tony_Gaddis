def main():
    russian = input('Русский язык: ')
    print('\nМолодёжный жаргон:', end=' ')
    print(convert_language(russian))


def convert_language(text):
    list_rus = text.split()
    list_young = []
    for word in list_rus:
        word_young = (word[1:] + word[0] + 'ки').upper()#, end=' ')
        list_young.append(word_young)
        young = ' '.join(list_young)
    return young


main()