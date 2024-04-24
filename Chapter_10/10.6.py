class Patient:
    def __init__(self, patient_name, patient_address, patient_phone, emergency_contact):
        self.name = patient_name
        self.address = patient_address
        self.phone = patient_phone
        self.emerg_cont = emergency_contact
    
    def set_name(self, patient_name):
        self.name = patient_name
    def set_address(self, patient_address):
        self.address = patient_address
    def set_phone(self, patient_phone):
        self.phone = patient_phone
    def set_emergency_contact(self, emergency_contact):
        self.emerg_cont = emergency_contact
    
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_phone(self):
        return self.phone
    def get_emergency_contact(self):
        return self.emerg_cont

    def __str__(self):
        return f'Пациент: {self.name}\n' \
               f'Адрес пациента: {self.address}\n' \
               f'Телефон пациента: {self.phone}\n' \
               f'Имя и телефон контактного лица для экстренной связи: {self.emerg_cont}'


class Procedure:
    def __init__(self, title_procedure, date_procedure,
                 doctor_of_procedure, price_procedure):
        self.title = title_procedure
        self.date = date_procedure
        self.doctor = doctor_of_procedure
        self.price = price_procedure
        
    def set_title_procedure(self, title_procedure):
        self.title = title_procedure
    def set_date_procedure(self, date_procedure):
        self.date = date_procedure
    def set_doctor_of_procedure(self, doctor_of_procedure):
        self.doctor = doctor_of_procedure
    def set_price_procedure(self, price_procedure):
        self.price = price_procedure

    def get_title_procedure(self):
        return self.title
    def get_date_procedure(self):
        return self.date
    def get_doctor_of_procedure(self):
        return self.doctor
    def get_price_procedure(self):
        return self.price

    def __str__(self):
        return f'\tНазвание процедуры: {self.title}\n' \
               f'\tДата: {self.date}\n' \
               f'\tВрач: {self.doctor}\n' \
               f'\tСтоимость: {self.price}'


def main():
    print("Введите данные  пациенте: ")
    patient = input_info_patient()
    procedure_list = input_info_procedure()
    print('-' * 20, '\n')
    output_info_patient(patient)
    output_info_procedure(procedure_list)
    print('-' * 20)
    total_sum(procedure_list)


def input_info_patient():
    patient_name = input('ФИО пациента: ')
    patient_address = input('Адрес пациента: ')
    patient_phone = input('Телефон пациента: ')
    emergency_contact = input('Имя и телефон контактного лица для экстренной связи:\n')

    patient = Patient(patient_name, patient_address, patient_phone, emergency_contact)
    return patient


def input_info_procedure():
    procedure_1 = Procedure('Врачебный осмотр', '20.04.2024', 'Ирвин', 250.00)
    procedure_2 = Procedure('Рентгенография', '02.05.2024', 'Джемисон', 500.00)
    procedure_3 = Procedure('Анализ крови', '26.04.2024', 'Смит', 200.00)
    proc_lst = [procedure_1, procedure_2, procedure_3]
    return proc_lst


def output_info_patient(patient):
    print(patient)
    print()


def output_info_procedure(proc_lst):
    for i in range(len(proc_lst)):
        print(f'Процедура №{i + 1}:')
        print(proc_lst[i])


def total_sum(proc_lst):
    total_sum = 0
    for procedure in proc_lst:
        total_sum += procedure.price
    print('Общая сумма расходов на процедуры:', total_sum)


main()
