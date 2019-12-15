"""
4. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. Например,
если было введено "abc cde def", то должно быть выведено "abcdef".
"""

n = input()
result = ''
for i in n.replace(' ', ''):
    if i not in result:
        result += i
print(result)
