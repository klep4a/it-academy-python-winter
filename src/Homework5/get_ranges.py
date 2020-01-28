"""Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    temp_list = []
    ranges_list = []
    for i in lst:
        if i + 1 not in lst or i - 1 not in lst:
            temp_list.append(i)
            if i + 1 not in lst:
                ranges_list.append(temp_list.copy())
                temp_list.clear()
    for r in ranges_list:
        if len(r) > 1:
            temp_list.append('-'.join(str(el) for el in r))
        else:
            temp_list.append(str(r[0]))
    return ','.join(temp_list)


lst = [0, 1, 2, 3, 4, 7, 8, 10]
print(get_ranges(lst))
