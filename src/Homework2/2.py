"""
https://www.hackerrank.com/klep4a
"""

# https://www.hackerrank.com/challenges/python-print

"""
Print Function

Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "" represents the values in between.

Input Format

The first line contains an integer N.

Output Format

Output the answer as explained in the task.
"""

if __name__ == '__main__':
    n = int(input())
for i in range(1, n + 1):
    print(i, end='')

# https://www.hackerrank.com/challenges/python-loops

"""
Loops

Task
Read an integer N. For all non-negative integers i < N, print i**2.
See the sample for details.

Input Format

The first and only line contains the integer, N.

Constraints
1 <= N <= 20

Output Format

Print N lines, one corresponding to each i.
"""

if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i**2)

# https://www.hackerrank.com/challenges/string-validators

"""
String Validators

Task

You are given a string S.
Your task is to find out if the string S contains: alphanumeric
characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string S.

Constraints
0 < len(S) < 1000

Output Format

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
"""

if __name__ == '__main__':
    s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))

# https://www.hackerrank.com/challenges/capitalize

"""
Capitalize!

You are asked to ensure that the first and last names of people
begin with a capital letter in their passports. For example,
alison heck should be capitalised correctly as Alison Heck.

alison heck --> Alison Heck

Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, S.

Constraints
    0 < len(S) < 1000

    The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example
12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, S.
"""

s = input()


def solve(s):
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s

print(solve(s))

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

"""
Find the Runner-Up Score!

Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given n scores.
Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[ ] of
n integers each separated by a space.

Constraints
    2 <= n <= 10
    -100 <= A[i] <=100

Output Format

Print the runner-up score.
"""

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

"""
Find a string

In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs
in the given string. String traversal will take place from left
to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string.
The next line contains the substring.

Constraints
    1 <= len(string) <= 200

Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences
of the substring in the original string.

"""


def count_substring(string, sub_string):
    x = 0
    for i in range(0, len(string) - len(sub_string) + 1, 1):
        item = string[i:(i + len(sub_string))]
        if item == sub_string:
            x += 1
    return x

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
