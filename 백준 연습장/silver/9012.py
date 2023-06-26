# https://www.acmicpc.net/problem/9012

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    count = 0
    vps = sys.stdin.readline().strip()
    for char in list(vps):
        if len(vps) % 2 != 0:
            print('NO')
            break
        if not stack:
            if char == ')':
                print('NO')
                break
            else:
                stack.append(char)
                count += 1
                continue
        if char == '(':
            stack.append(char)
            count += 1
        else:
            if stack:
                stack.pop()
                count += 1
                if not stack and count == len(vps):
                    print('YES')
                    break
        if stack and count == len(vps):
            print('NO')
            break
