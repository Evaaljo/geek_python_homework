'''Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

with open('my_text.txt') as f:
    lines = f.readlines()
    expanded_lines = [line.split() for line in lines]

lines_count, words_count = len(lines), sum([len(word_list) for word_list in expanded_lines])

print(f"Всего строк - {lines_count}, всего слов - {words_count}")

