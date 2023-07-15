# https://www.acmicpc.net/problem/11279

import heapq
import sys

max_heap = []

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        try:
            print(heapq.heappop(max_heap)[1])
        except IndexError:
            print(0)
    else:
        heapq.heappush(max_heap, (-num, num))
