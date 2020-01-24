"""
2. Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""

from datetime import datetime


def nod_evklid(big=0, small=0):
    """Computing the greatest common divisor (GCD) of two numbers ==
    naibolshiy obschiy delitel (NOD) dvuh chisel in russian translit,
    using the Euclidean algorithm and print them.


    Args:
    two numbers
    Return:
    one number == GCD (default == 0)
    """
    print('Привет! Я функция {}, я делаю {}'.
          format(nod_evklid.__name__, nod_evklid.__doc__))
    while big and small:
        if big > small:
            big %= small
        else:
            small %= big
    print('Наибольший общий делитель =', big + small)
    return big + small


def decor_result(func):
    def wr(*self):
        with open('results.txt', 'a') as file:
            file.write('Я функция: {} '
                       'Result: {}  {}\n'.format(func.__name__,
                                                 func(*self),
                                                 datetime.today()))
        return func
    return wr


nod_evklid_wrapped = decor_result(nod_evklid)
nod_evklid_wrapped()
nod_evklid_wrapped(1071, 462)
