# https://www.acmicpc.net/problem/1463

# 다이나믹 프로그래밍을 사용하여 해결하기 https://hongjw1938.tistory.com/47
N = int(input())
dp = [0] * (N + 1)  # N개의 배열 선언
dp[1] = 0

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        if dp[i//2] + 1 < dp[i]:
            dp[i] = dp[i//2] + 1
    if i % 3 == 0:
        if dp[i//3] + 1 < dp[i]:
            dp[i] = dp[i//3] + 1
print(dp[N])
# 접근을 잘못함
# count = 0
#
# while N != 1:
#     if N % 3 == 0:
#         N /= 3
#         count += 1
#     elif (N - 1) % 3 == 0:
#         N -= 1
#         count += 1
#     elif N % 2 == 0:
#         N /= 2
#         count += 1
#     else:
#         N -= 1
#         count += 1
# print(count)
