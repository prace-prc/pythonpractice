# https://www.acmicpc.net/problem/2606

import sys
from collections import deque

pc_num, connects = int(sys.stdin.readline()), int(sys.stdin.readline())

maps = {i + 1: [] for i in range(pc_num)}

for _ in range(connects):
    a, b = map(int, sys.stdin.readline().split())
    maps[a].append(b)
    maps[b].append(a)

corrupted = [1]
queue = deque()
queue.append(1)

while queue:
    current = queue.popleft()
    for pc in maps[current]:
        if pc not in corrupted:
            corrupted.append(pc)
            queue.append(pc)

# for i in maps:
#     if i in corrupted:
#         corrupted.extend(maps[i])
#
# corrupted = set(corrupted)

# 이미 감염되어있던 1번 제외하고 계산
print(len(corrupted) - 1)