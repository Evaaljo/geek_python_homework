'''Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.'''

data_list = [7, 2.5, "David Neel", b"Nane", False, ["something", "somewhere", "ever"], None]

for item in data_list:
    print(type(item))
