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

dct_cities = {}
for _ in range(int(input('количество стран? '))):
    country, *cities = input('страна города через пробел? ').split()
    for city in cities:
        if city in dct_cities.keys():
            dct_cities[city] += [country]
        else:
            dct_cities[city] = [country]
request = []
for _ in range(int(input('число городов? '))):
    request.append(input('город? '))
for city in request:
    print(*dct_cities.get(city))
