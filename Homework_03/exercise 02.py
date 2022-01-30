'''Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.'''

def user_data(first_name, last_name, year_of_birth, city_of_residence, email, phone):
    return (first_name, last_name, year_of_birth, city_of_residence, email, phone)

user_first_name = input("Введите имя...")
user_last_name = input("Введите фамилию...")
user_year = (input("Введите год рождения..."))
user_city = input("Введите город проживания...")
user_email = input("Введите почту...")
user_phone = int(input("Введите номер телефона..."))
print(
    user_data(user_first_name, user_last_name, user_year, user_city, user_email, user_phone)
)
