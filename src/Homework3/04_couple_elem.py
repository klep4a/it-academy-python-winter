"""
4. Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

# It works with numbers and chars
lst = [x for x in input().split()]
dct_ = {}.fromkeys(lst)
for key in dct_.keys():
    couple = 0
    for indx, elem in enumerate(lst):
        if key == elem:
            couple += lst[indx + 1:].count(elem)
    dct_[key] = couple
print(sum(dct_.values()))
