# https://www.acmicpc.net/problem/17219
import sys

N, M = sys.stdin.readline().strip().split()

id_pass = {}

for _ in range(int(N)):
    site, pw = sys.stdin.readline().strip().split()
    id_pass[site] = pw

for _ in range(int(M)):
    search = sys.stdin.readline().strip()
    if search in id_pass:
        print(id_pass[search])