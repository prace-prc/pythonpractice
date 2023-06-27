# https://www.acmicpc.net/problem/1654

# # 반복을 사용한 방법 (아주 높은 값이 들어올 수 있어서 시간 초과)
# import sys
#
# K, N = map(int, sys.stdin.readline().split())
#
# lines = []
#
# for _ in range(K):
#     lines.append(int(sys.stdin.readline()))
#
# maxlen = sum(lines) // N
#
# for cut in range(maxlen, 1, -1):
#     count = 0
#     for length in lines:
#         count += length // cut
#     if count == N:
#         print(cut)
#         break

# 이진 탐색을 사용하는 방법
import sys


def count_lans(lines, N, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    count = sum(length // mid for length in lines)

    if count >= N:
        return max(mid, count_lans(lines, N, mid + 1, end))
    else:
        return count_lans(lines, N, start, mid - 1)


K, N = map(int, sys.stdin.readline().split())

lines = []

for _ in range(K):
    lines.append(int(sys.stdin.readline()))

result = count_lans(lines, N, 1, max(lines))
print(result)