# https://www.acmicpc.net/problem/2164

from collections import deque

top = int(input())

cards = deque()

for i in range(top):
    cards.append(i+1)

while len(cards) >= 2:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])