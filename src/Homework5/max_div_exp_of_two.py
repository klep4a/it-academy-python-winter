"""Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def div_exp_bit_length(num):
    div = num.bit_length() - 1
    while num % (1 << div):
        div -= 1
    return 1 << div


print(div_exp_bit_length(10))
