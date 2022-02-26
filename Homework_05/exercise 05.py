"""Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import randrange

random_list = [randrange(0, 500) for _ in range(50)]

with open("list_of_numbers.txt", "w+") as f_random:
    f_random.write(" ".join(map(str, random_list)))

print(f"Список чисел: {random_list}\nСумма чисел: {sum(random_list)}")
