'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

def division(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "На ноль делить нельзя."


a = int(input("Введите первое число..."))
b = int(input("Введите второе число..."))
print(division(a, b))
