# https://www.acmicpc.net/problem/10773
import sys

K = int(input())
numlist = []

for _ in range(K):
    n = int(sys.stdin.readline())
    if n != 0:
        numlist.append(n)
    else:
        numlist.pop()

print(sum(numlist) if numlist else 0)
