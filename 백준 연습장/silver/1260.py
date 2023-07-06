# https://www.acmicpc.net/problem/1260

import sys
from collections import deque


def dfs_iterative(start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))


def bfs_iterative(start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])


N, M, V = map(int, sys.stdin.readline().strip().split())

graph = {i + 1: [] for i in range(N)}  # 딕셔너리 컴프리헨션

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    graph[i + 1] = sorted(graph[i + 1])

dfs_iterative(V)
print()
bfs_iterative(V)
