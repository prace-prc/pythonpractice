# https://www.acmicpc.net/problem/10845

import sys
amount = int(sys.stdin.readline())
stack = []

for i in range(amount):
    msg = sys.stdin.readline()

    if 'push' in msg:
        stack.append(int(msg.split()[1]))
    elif 'pop' in msg:
        if stack:
            print(stack.pop(0))
        else:
            print(-1)
    elif 'size' in msg:
        print(len(stack))
    elif 'empty' in msg:
        print(0 if stack else 1)
    elif 'front' in msg:
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif 'back' in msg:
        if stack:
            print(stack[-1])
        else:
            print(-1)