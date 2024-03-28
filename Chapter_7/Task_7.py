def check_answers(correct_answers, student_answers):
    incorrect_answer_count = 0
    correct_answer_count = 0
    incorrect_answers = []
    for i in range(len(correct_answers)):
        if correct_answers[i] != student_answers[i]:
            incorrect_answer_count += 1
            incorrect_answers.append(i + 1)
        else:
            correct_answer_count += 1
    return correct_answer_count, incorrect_answer_count, incorrect_answers


corr_ans = open('answers.txt', 'r').readlines()

stud_ans = open('Student_Solution.txt', 'r').readlines()

corr_ans_count, incorr_ans_count, incorr_ans = check_answers(corr_ans, stud_ans)

if corr_ans_count >= 15:
    print('Экзамен сдан.')
else:
    print('Экзамен не сдан.')
print('Правильных ответов:', corr_ans_count,
      '\nНеправильных ответов:', incorr_ans_count,
      '\nНеправильные ответы на вопросы:', incorr_ans)
