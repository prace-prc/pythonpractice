# https://www.acmicpc.net/problem/15829

L = int(input())
string = input()

hash = 0

for i, c in enumerate(list(string)):
    hash += (ord(c)-96) * 31**i

hash %= 1234567891

print(hash)