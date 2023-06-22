# https://www.acmicpc.net/problem/10989
import sys

# 수가 천만까지 들어가서 메모리 초과가 발생함
# nums = []
# for i in range(int(sys.stdin.readline())):
#     nums.append((sys.stdin.readline()))
# nums.sort()
# print(''.join(nums))

# 수가 10000까지 들어가므로 10000 크기의 배열을 만들고 출력시 불러오는 방식
n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)