# https://www.acmicpc.net/problem/2675

t = int(input())
result = ""

for i in range(t):
    r, s = input().split()
    for n in range(len(s)):
        result += s[n] * int(r)
    print(result)
    result = ""