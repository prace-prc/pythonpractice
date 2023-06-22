# https://www.acmicpc.net/problem/18111
import sys

# 입력 받음
n, m, b = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 0~256까지가 땅의 범위임. 0~256까지 체크하면 답은 나오나 시간 초과.
min_height = sys.maxsize
max_height = 0
for i in range(n):
    for j in range(m):
        min_height = min(min_height, field[i][j])
        max_height = max(max_height, field[i][j])

min_time = sys.maxsize  # 값을 최대값으로 하는 이유 :  min_time을 초기에 0으로 설정한다면, 첫 번째 시도한 시간이 항상 최소 시간이 되어버리므로 올바른 결과를 얻을 수 없다
optimal_height = 0

for h in range(min_height, max_height + 1):
    blocks = b
    time = 0
    for i in range(n):
        for j in range(m):
            diff = field[i][j] - h
            if diff > 0:  # 현재 높이보다 큰 경우, 블록을 제거함
                blocks += diff
                time += diff * 2
            elif diff < 0:  # 현재 높이보다 작은 경우, 블럭을 설치함
                blocks += diff
                time -= diff  # diff값이 음수이므로 더해주어야 함
    # 위의 계산을 실시 한 후 블록 갯수가 음수가 아닌(충분히 많이 가지고 있었을) 경우
    if blocks >= 0:
        if time <= min_time:  # 지금까지 계산한 것들 중 시간이 최소인 경우 또는 같은 경우 땅의 높이가 더 높은 경우
            min_time = time
            optimal_height = h

print(min_time, optimal_height)

# 3일동안 고민했는데 대실패.. 개념을 이해를 못했음
# n, m, b = map(int, sys.stdin.readline().split())
# field = []
# fmin, fmax = -1, 0
# time = 0
#
# for i in range(n):
#     field.append(list(map(int, sys.stdin.readline().split())))
#     if max(field[i]) > fmax:
#         fmax = max(field[i])
#     if fmin == -1:
#         fmin = min(field[i])
#     if min(field[i]) < fmin:
#         fmin = min(field[i])
#
#
# field_val = {}
#
# for i in field:
#     for j in i:
#         if j not in field_val:
#             field_val[j] = 1
#         else:
#             field_val[j] += 1
#
# most_block = [k for k, v in field_val.items() if v == max(field_val.values())]
#
# less_block = 0
#
# for i in field:
#     for j in i:
#         if j > most_block[0]:
#             time += (j - most_block[0]) * 2
#             b += 1
#         elif j < most_block[0]:
#             less_block += most_block[0] - j
#             if less_block <= b:
#                 time += 1
#                 less_block -= 1
#                 b -= 1
#             else:
#                 time += (j - most_block[0]) * 2
#                 b += 1
#
# print(less_block)
#
# print(time, most_block[0])
