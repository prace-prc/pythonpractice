# https://www.acmicpc.net/problem/10952

num_list = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    num_list.append((a,b))
for x,y in num_list:
    print(x+y)