"""
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета. 
Output: Общая цена 9 рублей 60 копеек
"""

n = input().split()
basket = []
for i in n:
    if i.isdigit():
        basket.append(int(i))
cost_kop = (basket[0] * 100 + basket[1]) * basket[2]        
print('Общая цена', cost_kop // 100, 'рублей', cost_kop % 100, 'копеек.')
