# https://www.acmicpc.net/problem/18111
import sys

n, m, b = map(int, sys.stdin.readline().split())
field = []
fmin, fmax = -1, 0

for i in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))
    if max(field[i]) > fmax:
        fmax = max(field[i])
    if fmin == -1:
        fmin = min(field[i])
    if min(field[i]) < fmin:
        fmin = min(field[i])

print(field, fmax, fmin)
field_val = {}

for i in field:
    for j in i:
        if j not in field_val:
            field_val[j] = 1
        else:
            field_val[j] += 1

print(field_val)

