# https://www.acmicpc.net/problem/1676

N = int(input())


def get_fact(n):
    if (n > 1):
        return n * get_fact(n - 1)
    else:
        return 1


r_list = reversed(list(map(int, str(get_fact(N)))))
for i in range(N):  # N = 0일시 아예 수행을 안함
    if next(r_list) != 0:
        print(i)
        break
if N == 0:
    print(0)
