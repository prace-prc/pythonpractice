# https://www.acmicpc.net/problem/1929
a, b = map(int, input().split())

def isprime(n: int) -> bool:
    if n is not 1 :
        for i in range(2, int(n ** 0.5) + 1): # (n / 2)는 시간초과 발생, 시간복잡도가 더 높은거같음.
            if n % i == 0:
                return False
        return True

for i in range(a, b + 1):
    if isprime(i):
        print(i)

# 소수 구하는 알고리즘 - 에라토스테네스의 체 사용, 시간 복잡도 감소
#
# isprime = [True]*(b+1)
# isprime[1] = False
#
# for i in range(2,b+1):
#     for j in range(2,b+1):
#         if i*j > b:
#             break
#         isprime[i*j] = False
#
# for i in range(a,b+1):
#     if isprime[i]:
#         print(i)