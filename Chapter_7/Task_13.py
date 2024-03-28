import random

while True:
    answers = open('8_ball_responses.txt', 'r').read().splitlines()

    question = input('Ваш вопрос: ')
    if question == 'Стоп' or question == 'стоп':
        break
    i = random.randint(0, len(answers))
    print(answers[i])
    print('\nЕсли надоело, наберите \'Стоп\'')

