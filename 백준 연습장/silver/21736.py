# https://www.acmicpc.net/problem/21736
import sys
global people_count

sys.setrecursionlimit(10**4)

people_count = 0

N, M = map(int, input().split())

campus_map = []
for _ in range(N):
    campus_map.append(list(sys.stdin.readline().strip()))


def dfs(grid, i, j):
    global people_count
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'X':
        return
    if grid[i][j] == 'P':
        people_count += 1
    grid[i][j] = 'X'
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)


for i in range(N):
    for j in range(M):
        if campus_map[i][j] == 'I':
            dfs(campus_map, i, j)

print(people_count if people_count != 0 else 'TT')