"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
a. runner() – все фукнции вызываются по очереди
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


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
    # if not big or small:
    #     big = int(input('Введите первое число: '))
    #     small = int(input('Введите второе число: '))
    while big and small:
        if big > small:
            big %= small
        else:
            small %= big
    print('Наибольший общий делитель =', big + small)
    return big + small


def num_intersect(lst1=[1, 2, 3], lst2=[0, 1, 2]):
    """Return and print the quantity of
    elements intersection of two lists.
    (i.e. quantity of all elements that are in both lists.)


    Args:
    two lists (default is [1, 2, 3] and [0, 1, 2])
    Return:
    one number == quantity of elements intersection (default == 2)
    """
    print('Привет! Я функция {}, я делаю {}'.
          format(num_intersect.__name__, num_intersect.__doc__))
    print('Количество одинаковых элементов в двух списках =',
          len(set(lst1).intersection(set(lst2))))
    return len(set(lst1).intersection(set(lst2)))


def fizz_buzz():
    """FizzBuzz печатает цифры от 1 до 32,
    но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратных 5
    пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
    """
    print('Привет! Я функция {}, я делаю {}'.
          format(fizz_buzz.__name__, fizz_buzz.__doc__))
    for i in range(1, 32):
        print('Fizz' * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i, end=' ')


def runner(*funcs):
    all_funcs = {nod_evklid.__name__: nod_evklid,
                 num_intersect.__name__: num_intersect,
                 fizz_buzz.__name__: fizz_buzz}
    if funcs:
        for i in [*funcs]:
            all_funcs[i]()
    else:
        for i in all_funcs:
            all_funcs[i]()


runner()
# runner('num_intersect')
# runner('nod_evklid', 'fizz_buzz')
