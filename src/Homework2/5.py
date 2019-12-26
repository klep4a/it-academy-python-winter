"""
Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы.
"""

import string
n = input()
low_symb, upp_symb = 0, 0
for i in n:
    if i in string.ascii_lowercase:
        low_symb += 1
    elif i in string.ascii_uppercase:
        upp_symb += 1
print('строчных =', low_symb, 'прописных =', upp_symb)
