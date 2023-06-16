# https://www.acmicpc.net/problem/1920
num_list = []

for _ in range(2):
    amount = int(input())
    num_list.append(input().split())

intersection = (set(num_list[0]) & set(num_list[1]))

for i, n in enumerate(num_list[1]):
    if n in intersection:
        print(1)
    else:
        print(0)

