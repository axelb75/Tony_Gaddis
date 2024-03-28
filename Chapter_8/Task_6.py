text = open('text.txt', 'r').read().splitlines()

sum_word = 0
words = []
for sentence in text:
    word = len(sentence.split(' '))
    words.append(word)
    sum_word += word

print('\nСредднее количество слов в предложении:', int(sum_word / len(text)), 'слов.')
print('Количество слов в каждом предложении:\nПредложение:\tКоличество слов:')
for i in range(len(text)):
    print(f'\t{i + 1}\t\t\t\t{words[i]}')