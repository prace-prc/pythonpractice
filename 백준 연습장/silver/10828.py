# https://www.acmicpc.net/problem/10828
import sys
amount = int(sys.stdin.readline())
stack = []

# def push(x: int):
#     stack.append(x)
#
# def pop():
#     if stack:
#         print(stack.pop())
#     else:
#         print(-1)
#
# def size():
#     print(len(stack))
#
# def empty():
#     print(0 if stack else 1)
#
# def top():
#     if stack:
#         print(stack[-1])
#     else:
#         print(-1)


for i in range(amount):
    msg = sys.stdin.readline()

    if 'push' in msg:
        stack.append(int(msg.split()[1]))
    elif 'pop' in msg:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in msg:
        print(len(stack))
    elif 'empty' in msg:
        print(0 if stack else 1)
    elif 'top' in msg:
        if stack:
            print(stack[-1])
        else:
            print(-1)
