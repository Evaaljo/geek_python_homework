# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input("Введите число >>>"))
n_1 = int(f'{n}{n}')
n_2 = int(f'{n}{n}{n}')
n_3 = n + n_1 + n_2

print(f"{n} + {n_1} + {n_2} = {n_3}")