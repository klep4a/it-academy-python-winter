"""
2. Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""

from datetime import datetime
from runner_funcs import nod_evklid
from runner_funcs import runner


def decor_result(func):
    def wr(*args, **kwargs):
        with open('results.txt', 'a') as f:
            f.write('I am function: {} '
                    'Result: {}  {}\n'.format(func.__name__,
                                              func(*args, **kwargs),
                                              str(datetime.today())[:-10]))
        return func
    return wr


nod_evklid_wrapped = decor_result(nod_evklid)
nod_evklid_wrapped()
nod_evklid_wrapped(1071, 462)
runner_wrapped = decor_result(runner)
runner_wrapped()
runner_wrapped('fizz_buzz')
