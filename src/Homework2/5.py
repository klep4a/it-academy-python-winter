"""
Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы.
"""

n = input()
low_symb, upp_symb = 0, 0
for i in n:
    if 'a' <= i <= 'z':
        low_symb += 1
    elif 'A' <= i <= 'Z':
        upp_symb += 1
print(upp_symb, low_symb)
