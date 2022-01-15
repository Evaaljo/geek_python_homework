# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
n = int(input("Введите целое число >>>"))

max_n = 0
while n and max_n != 9:
    print(n)
    current = n % 10
    n = n // 10
    max_n = current if current > max_n else max_n

print(max_n)