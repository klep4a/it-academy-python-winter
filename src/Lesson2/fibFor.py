n = int(input('Введите число искомых чисел Фибоначчи '))
fib = 0
fib1 = 1
for i in range(n):
    print(fib, end=' ')
    fib, fib1 = fib + fib1, fib
