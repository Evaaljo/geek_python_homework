'''Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.'''

def my_func(number_1, number_2, number_3):
    numbers = [number_1, number_2, number_3]
    numbers.remove(min(numbers))
    return sum(numbers)

a = int(input("Введите первое число... "))
b = int(input("Введите второе число... "))
c = int(input("Введите третье число... "))
print(my_func(a, b, c))
