"""
4. Вводится строка. Требуется удалить из нее повторяющиеся
символы и все пробелы. Например, если было введено
"abc cde def", то должно быть выведено "abcdef".
"""

import string
n = input()
result = ''
for i in n:
    if i not in result and i not in string.whitespace:
        result += i
print(result)
