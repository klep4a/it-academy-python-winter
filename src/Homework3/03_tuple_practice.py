"""
3. Tuple practice
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
Создайте кортеж из одного элемента, чтобы при итерировании по этому
элементы последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""

tpl = tuple(['a', 'b', 'c'])
lst = list(('a', 'b', 'c'))
print(tpl, lst, tpl == tuple(lst), lst == list(tpl))
#>>> ('a', 'b', 'c') ['a', 'b', 'c'] True True
tpl, lst = ('a', 2, 'python'), ['a', 2, 'python']
print(tpl, lst)
#>>> ('a', 2, 'python') ['a', 2, 'python']
tpl = (
    '123',
)
for x in tpl[0]:
    print(x, type(tpl), len(tpl))
"""
1 <class 'tuple'> 1
2 <class 'tuple'> 1
3 <class 'tuple'> 1
"""