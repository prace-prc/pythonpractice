# https://www.acmicpc.net/problem/2108

import sys

N = int(sys.stdin.readline())
nums = []
# 절대값 범위의 리스트 만들어서 비교한 버전. 실행시간 1350ms
# num_seen = [0] * 8001  # 절대값 4천이 N의 범위
#
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     nums.append(num)
#     num_seen[num + 4000] += 1
#
# # 산술평균
# print(round((sum(nums) / N)))
# # 중앙값
# print(sorted(nums)[N // 2])
# # 최빈값
# max_seen = list(filter(lambda x: num_seen[x] == max(num_seen), range(8001)))
# if len(max_seen) >= 2:
#     print(max_seen[1]-4000)
# else:
#     print(max_seen[0]-4000)
# # 범위
# print(max(nums) - min(nums))

# 딕셔너리 사용한 버전. 실행시간 480ms
num_seen = {}

for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
    # 딕셔너리에 저장, 키가 존재하지 않는 딕셔너리는 호출하면 오류가 나서 이렇게 구현해봤는데 - if num in num_seen - 보다 더 좋은가?
    try:
        num_seen[num] += 1
    except KeyError:
        num_seen[num] = 1

# 산술평균
print(round((sum(nums) / N)))
# 중앙값
print(sorted(nums)[N // 2])
# 최빈값
max_seen = max(num_seen.values())
modes = [num for num, count in num_seen.items() if count == max_seen]
modes.sort()
print(modes[1] if len(modes) > 1 else modes[0])
# 범위
print(max(nums) - min(nums))
