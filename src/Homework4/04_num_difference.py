"""
Даны два списка чисел. Посчитайте, сколько различных 
чисел входит только в один из этих списков
"""

lst1 = [*range(100)[::2]]
lst2 = [*range(100)[::3]]
print('Всего различных чисел из двух списков =',
      len(set(lst1).symmetric_difference(set(lst2))))
print('В списке 1 чисел отличных от списка 2 =',
      len(set.difference(set(lst1), set(lst2))))
print('В списке 2 чисел отличных от списка 1 =',
      len(set.difference(set(lst2), set(lst1))))
