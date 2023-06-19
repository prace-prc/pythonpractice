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
#
#
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
# # 깊이 우선 탐색(DFS)
# visited = set()
#
#
# def dfs_iterative(start_node):
#     stack = [start_node]
#
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             stack.extend(reversed(graph[node]))
#
#
# snode = 'A'
# dfs_iterative(snode)
#
# print('\n------')
#
# # 너비 우선 탐색(BFS)
# visited = set()
# def bfs_iterative(start_node):
#     queue = deque([start_node])
#
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             queue.extend(graph[node])
#
# bfs_iterative(snode)
#
# # urllib request
#
# import urllib.request
#
# url = 'https://www.google.com'
#
# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)
#
# html = response.read()
#
# print(html)
#
# # 이미지 파서 만들기
#
# from urllib.request import urlopen, urlretrieve
# from html.parser import HTMLParser
# from pathlib import Path
# from urllib.parse import urljoin, urlunparse
#
#
# class ImageParser(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.result = []
#
#     def handle_starttag(self, tag, attrs):
#         if tag != 'img':
#             return
#         if not hasattr(self, 'result'):
#             self.result = []
#         for name, value in attrs:
#             if name == 'src':
#                 self.result.append(value)
#
#
# def parse_image(data):
#     parser = ImageParser()
#     parser.feed(data)
#     data_set = set(x for x in parser.result)
#     return data_set
#
#
# # 이미지 다운로드 실습
# def download_image(url, data):
#     download_dir = Path('DOWNLOAD')
#     download_dir.mkdir(exist_ok=True)
#
#     parser = ImageParser()
#     parser.feed(data)
#     data_set = set(x for x in parser.result)
#     for x in sorted(data_set):
#         image_url = urljoin(url, x)
#         basename = Path(image_url).name
#         target_file = download_dir / basename
#         print(target_file)
#
#         print('Downloading...', image_url)
#         urlretrieve(image_url, target_file)
#
#
# def main():
#     # url = 'https://google.co.kr'
#     # with urlopen(url) as f:
#     #     charset = f.headers.get_params('charset')[1][1]
#     #     data = f.read().decode(charset)
#     host = 'www.google.co.kr'
#     conn = http.client.HTTPConnection(host)
#     conn.request('GET', '')
#     resp = conn.getresponse()
#
#     charset = resp.msg.get_param('charset')
#     print('charset:', charset)
#     data = resp.read().decode(charset)
#     conn.close()
#
#     print('\n>>>>> Downloading...', host)
#     url = urlunparse(('http', host, '', '', '', ''))
#
#     # data_set = parse_image(data)
#     # print('\n>>>>> Fetch Images from', url)
#     # print('\n'.join(sorted(data_set)))
#     download_image(url, data)
#
#
# if __name__ == '__main__':
#     main()

from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello World")


server = HTTPServer(("", 8080), SimpleHTTPRequestHandler)
server.serve_forever()

