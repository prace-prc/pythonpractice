# https://www.acmicpc.net/problem/11399

import sys

n = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().strip().split()))

total_time = 0
time_sum = 0
p.sort()
for t in p:
    total_time += t
    time_sum += total_time
print(time_sum)
