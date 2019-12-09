a, b, c = float(input()), float(input()), float(input())
if a + b > c and b + c > a and c + a > b:
    print('yes')
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** .5
    print(s)
else:
    print('not valid input')
