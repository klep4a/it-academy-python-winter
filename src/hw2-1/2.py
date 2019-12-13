"""
https://www.hackerrank.com/klep4a
"""

# https://www.hackerrank.com/challenges/python-print

if __name__ == '__main__':
    n = int(input())
for i in range(1, n + 1):
    print(i, end='')

# https://www.hackerrank.com/challenges/python-loops

if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i**2)

# https://www.hackerrank.com/challenges/string-validators

if __name__ == '__main__':
    s = input()
print (any(c.isalnum() for c in s))
print (any(c.isalpha() for c in s))
print (any(c.isdigit() for c in s))
print (any(c.islower() for c in s))
print (any(c.isupper() for c in s))

# https://www.hackerrank.com/challenges/capitalize

s = input()

def solve(s):
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s

print(solve(s))

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
max = arr[0]
for i in arr:
    if i >= max:
        max = i
for i in sorted(arr, reverse=True):
    if i < max:
        print(i)
        break

# https://www.hackerrank.com/challenges/find-a-string

def count_substring(string, sub_string):
    x=0
    for i in range(0, len(string) - len(sub_string) + 1, 1):
        item = string[i:(i+len(sub_string))]
        if item == sub_string:
        # numitem = i
        # print(numitem, end=' ')
            x += 1
    return x

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()    
    count = count_substring(string, sub_string)
    print(count)

# как есть, так есть :-)
