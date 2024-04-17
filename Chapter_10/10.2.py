class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def to_break(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def get_info(self):
        return f'Автомобиль {self.__year_model} года выпуска, марки {self.__make}'


car_1 = Car(1978, 'Ford')
print(car_1.get_info(), '\n', '-' * 20)
for i in range(5):
    car_1.accelerate()
    print(f'Газуем\tТекущая скорость: {str(car_1.get_speed())}')

for i in range(5):
    car_1.to_break()
    print(f'Тормозим\tТекущая скорость: {str(car_1.get_speed())}')