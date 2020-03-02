"""Создайте декоратор, который вызывает задекорированную функцию
 пока она не выполнится без исключений (но не более n раз -
  параметр декоратора). Если превышено количество попыток,
   должно быть возбуждено исключение типа TooManyErrors
"""


def count_errors(errors):
    count = 0

    def decorator(f):
        def wrapper(*args, **kw):
            nonlocal count
            try:
                return f(*args, **kw)
            except Exception as e:
                count += 1
                while count < errors:
                    return e.args[0]
                print('TooManyErrors')
                raise
        return wrapper
    return decorator


@count_errors(3)
def div(a, b):
    return a / b


print(div(1, 2))
print(div(1, 0))
print(div(1, '2'))
print(div(1, None))
