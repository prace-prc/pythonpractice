# https://www.acmicpc.net/problem/2579

import sys
n = int(sys.stdin.readline())

scores = [int(sys.stdin.readline()) for _ in range(n)]


# n을 저장 못하는 리스트 컴프리헨션
# scores = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
if n < 3:
    print(sum(scores))
else:
    dp = [0] * n
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])

    print(dp[-1])