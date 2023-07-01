# https://www.acmicpc.net/problem/18110

import sys


def make_round(num, i=0): # 파이썬 기본 round() 함수는 0.5를 반올림하는 과정에서 무조건 가까운 짝수를 찾아간다고 함. 그래서 따로 만들어야 함. 이런걸 어떻게알아..
    num = num * 10 ** i
    if num >= 0:
        num_f = int(num) + 1
        if num - int(num) >= 0.5:
            return int(num_f / (10 ** i))
        else:
            return int(num / (10 ** i))


n = int(sys.stdin.readline())

trim = make_round(n * 0.15)  # 앞뒤에서 자를 인원 수

dif_list = []

for _ in range(n):
    difficulty = int(sys.stdin.readline())
    dif_list.append(difficulty)

dif_list.sort()

if trim == 0:
    print(make_round(sum(dif_list) / (len(dif_list))) if n != 0 else 0)
else:
    print(make_round(sum(dif_list[trim:-trim]) / (len(dif_list) - trim * 2)))
