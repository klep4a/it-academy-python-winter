"""
2. List practice
Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить
следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий
['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка
и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так
чтобы в исходном списке этого элемента не было.
"""

lst1 = [x + y for x in 'ab' for y in 'bcd']
print(lst1)
lst2 = lst1[::2]
print(lst2)
lst3 = [str(x) + 'a' for x in range(1, 5)]
print(lst3)
print(lst3.pop(lst3.index('2a')))
print(lst3, id(lst3))
lst3_copy = lst3[:]
lst3_copy.insert(lst3.index('1a') + 1, '2a')
print(lst3_copy, id(lst3_copy))
