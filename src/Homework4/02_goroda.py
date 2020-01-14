"""
Города
Дан список стран и городов каждой страны. Затем даны названия
городов. Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия
городов этой страны. В следующей строке записано число M, далее
идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором
находится данный город.
Примеры
Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa    
3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
"""

dct_sities = {}
for i in(range(int(input('количество стран? ')))):
    line = input('строка? ').split()
    dct_sities.update({}.fromkeys(line[1:], line[0]))
request = []
for i in range(int(input('число городов? '))):
    request.append(input('город? '))
for x in request:
    print(dct_sities.get(x))
