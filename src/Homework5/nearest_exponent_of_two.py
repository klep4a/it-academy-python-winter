"""Написать программу которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1)
"""


def near_exp_bit_length(num):
    maxi, mini = 1 << num.bit_length(), 1 << (num.bit_length() - 1)
    if maxi - num < abs(mini - num):
        return maxi
    elif maxi - num > abs(mini - num):
        return mini
    else:
        return 'Таких числа два: {} {}'.format(maxi, mini)


print(near_exp_bit_length(48))
