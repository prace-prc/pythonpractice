# https://www.acmicpc.net/problem/2884

h, m = map(int, input().split())
if m - 45 < 0:
    m += 15  # m = m - 45 + 60
    h = 23 if h == 0 else h - 1
else:
    m -= 45
print(h, m)
