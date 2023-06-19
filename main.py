# # https://leetcode.com/problems/linked-list-cycle/
# # 풀이 1 Set 사용
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         node_seen = set()
#         while head is not None:
#             if head in node_seen:
#                 return True
#             node_seen.add(head)
#             head = head.next
#         return False
#
#
# # 풀이 2 러너 사용
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if not head or not head.next:
#             return False
#
#         slow = head
#         fast = head.next
#
#         while slow != fast:
#             if not fast or not fast.next:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True
from collections import deque

# https://leetcode.com/problems/number-of-islands/submissions/974400916/
#
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#
#         def dfs(grid, i, j):
#             if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
#                 return
#             grid[i][j] = '0'
#             dfs(grid, i - 1, j)
#             dfs(grid, i + 1, j)
#             dfs(grid, i, j - 1)
#             dfs(grid, i, j + 1)
#
#         island_count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     dfs(grid, i, j)
#                     island_count += 1
#
#         return island_count


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
# 깊이 우선 탐색(DFS)
visited = set()


def dfs_iterative(start_node):
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))


snode = 'A'
dfs_iterative(snode)

print('\n------')

# 너비 우선 탐색(BFS)
visited = set()
def bfs_iterative(start_node):
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

bfs_iterative(snode)