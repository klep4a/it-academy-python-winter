"""Создайте декоратор, который вызывает задекорированную функцию
 пока она не выполнится без исключений (но не более n раз -
  параметр декоратора). Если превышено количество попыток,
   должно быть возбуждено исключение типа TooManyErrors
"""


def count_errors(max_errors, runs):
    def decorator(func):
        def wrapper(*args, **kw):
            calls = 0
            errors = 0

            class TooManyErrors(Exception):
                pass

            for _ in range(runs):
                calls += 1
                try:
                    res = func(*args, **kw)
                    print((f'Call {calls} to "{func.__name__}",'
                           f' Errors: {errors}, Result: {res}'))
                except Exception as e:
                    errors += 1
                    if errors > max_errors:
                        res = e.args[0]
                        raise TooManyErrors(
                            f'Call {calls} to "{func.__name__}",'
                            f' Errors: {errors}, Result: {res}'
                        )
                    res = e.args[0]
                    print((f'Call {calls} to "{func.__name__}",'
                           f' Errors: {errors}, Result: {res}'))
        return wrapper
    return decorator


@count_errors(max_errors=2, runs=4)
def div(a, b):
    return a / b


div(1, 2)
div(1, None)
