# https://www.acmicpc.net/problem/10866

import sys

amount = int(sys.stdin.readline())
stack = []

for i in range(amount):
    msg = sys.stdin.readline()

    if 'push_back' in msg:
        stack.append(int(msg.split()[1]))
    elif 'push_front' in msg:
        stack.insert(0, int(msg.split()[1]))
    elif 'pop_front' in msg:
        if stack:
            print(stack.pop(0))
        else:
            print(-1)
    elif 'pop_back' in msg:
        if stack:
            print(stack.pop())
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
