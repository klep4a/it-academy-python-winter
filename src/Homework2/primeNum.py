n = int(input('Введите целое число\n'))
delitel = 2
flag = 0
while delitel**2 <= abs(n) and not flag:
    if n % delitel:
        delitel += 1
    else:
        flag = 1
if flag:
    print(n, 'Составное число\nДелитель равен', delitel)
else:
    print(n, 'Простое число')
