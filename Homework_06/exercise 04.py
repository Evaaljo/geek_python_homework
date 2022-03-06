"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed, color, name) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name}: начало движения")

    def stop(self):
        print(f"{self.name}: остановка")

    def turn(self, direction: str):
        print(f"{self.name}: поворот - {direction}")

    def show_speed(self):
        print(f"{self.name}: скорость = {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name}: Превышение допустимой скорости")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}: Превышение допустимой скорости")


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police: bool = True


cars = [
    TownCar(204, "blue", "Volkswagen"),
    SportCar(269, "gold", "Nissan"),
    WorkCar(90, "white", "Mercedes"),
    PoliceCar(180, "black", "Chevrolet")
]

cars[0].go()
cars[0].turn("налево")
cars[0].stop()

for car in cars:
    car.show_speed()
