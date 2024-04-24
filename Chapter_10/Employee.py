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

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'ID: {self.id}\n' \
               f'Отдел: {self.dept}\n' \
               f'Должность: {self.post}'