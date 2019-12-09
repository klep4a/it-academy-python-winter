var = int(input('Введите число\n'))
if var == 0:
    print('на нет спроса нет')
elif var % 2:
    print('OGO')
else:
    print('AGA')
    if var < 0:
        print('malovato')
    else:
        print('normalno')
