class Employee:
    def __init__(self, name, id, dept, post):
        self.name = name
        self.id = id
        self.dept = dept
        self.post = post
    
    def set_name(self, name):
        self.name = name
    def set_id(self, id):
        self.id = id
    def set_dept(self, dept):
        self.dept = dept
    def set_post(self, post):
        self.post = post
    
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_dept(self):
        return self.dept
    def get_post(self):
        return self.post


def main():
    employee_list = []
    for i in range(3):
        input_info(employee_list, i)
    
    print('Наши сотрудники:')
    for i in range(len(employee_list)):
        print(f'{i + 1} сотрудник:')
        output_info(employee_list[i])


def input_info(list, i):
    employee_name = input(f'Имя {i + 1}-го сотрудника: ')
    employee_id = int(input(f'Идентификационный номер {i + 1}-го сотрудника: '))
    employee_dept = input(f'Отдел {i + 1}-го сотрудника: ')
    employee_post = input(f'Должность {i + 1}-го сотрудника: ')
    print()
    employee = Employee(employee_name, employee_id, employee_dept, employee_post)
    list.append(employee)


def output_info(employee):
    print('\tИмя: {}\n\tИдентификационный номер: {}\n\tОтдел: {}\n\tДолжность: {}\n'.format(employee.name, employee.id, employee.dept, employee.post))
    

main()