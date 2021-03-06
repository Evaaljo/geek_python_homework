'''*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:

[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}'''

product_structure = {
    "Название": str,
    "Цена": int,
    "Количество": int,
    "Единица измерения": str,
}

product_list = []
product_counter = 1

while True:
    decision = input(f"Внести данные о новом товаре? [да/нет] ").lower()

    if decision == 'нет':
        break
    else:
        product_info = {}

        for characteristic_name, characteristic_type in product_structure.items():
            user_input = input(f"Введите данные '{characteristic_name}' >>> ")
            product_info[characteristic_name] = characteristic_type(user_input)

        product_list.append((product_counter, product_info))
        product_counter += 1

product_analytics = {}

for analytics_key in product_structure.keys():
    item_list = []

    for product in product_list:
        item_list.append(product[1][analytics_key])

    product_analytics[analytics_key] = set(item_list)

print(product_analytics)