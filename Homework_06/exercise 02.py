"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""


class Road:
    _length: float
    _width: float
    __weight: float = 25

    def __init__(self, length: float, width: float):
        self.weight = 25
        self._length = length
        self._width = width

    def calculate(self, thickness: float = 1):
        return (self._length * self._width * self.weight * thickness) / 100


asphalt = Road(20, 5000)
calculation = asphalt.calculate(5)

print(f"{calculation} т")
