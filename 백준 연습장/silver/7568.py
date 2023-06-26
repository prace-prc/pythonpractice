# https://www.acmicpc.net/problem/7568
import sys

N = int(sys.stdin.readline())
people = []

for _ in range(N):
    people.append(tuple(map(int, sys.stdin.readline().split())))


for person in people:
    rank = 1
    for other in people:
        if person[0] < other[0] and person[1] < other[1]:
            rank += 1
    print(rank, end=' ')