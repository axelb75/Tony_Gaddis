print('Задание 5. Проверка допустимости номера расходного счёта')
bank_accounts = open('charge_accounts.txt', 'r').readlines()
for i in range(len(bank_accounts)):
    bank_accounts[i] = int(bank_accounts[i].rstrip("\n"))

user_bank_account = int(input('Введите номер счёта: '))
if user_bank_account in bank_accounts:
    print('Номер допустимый.')
else:
    print('Номер недопустимый.')