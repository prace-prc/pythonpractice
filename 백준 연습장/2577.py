# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())
mul = a * b * c
num = [0] * 10
for i in str(mul):
    num[int(i)] += 1
for n in num:
    print(n)