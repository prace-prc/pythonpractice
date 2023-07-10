# https://www.acmicpc.net/problem/11723

import sys

M = int(sys.stdin.readline())

S = set()

for _ in range(M):
    line = sys.stdin.readline().strip()
    try:
        cmd, param = line.split()
        param = int(param)
    except ValueError:
        cmd = line
    if cmd == 'add':
        S.add(param)
    if cmd == 'remove':
        if param in S:
            S.remove(param)
    if cmd == 'check':
        print(1 if param in S else 0)
    if cmd == 'toggle':
        if param in S:
            S.remove(param)
        else:
            S.add(param)
    if cmd == 'all':
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    if cmd == 'empty':
        S = set()
