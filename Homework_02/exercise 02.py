'''Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().'''

numbers = input("Укажите значения через запятую >>> ").split(",")

max_idx = len(numbers) - 1

for idx in range(0, max_idx, 2):
    next_idx = idx + 1
    numbers[idx], numbers[next_idx] = numbers[next_idx], numbers[idx]

print(numbers)


