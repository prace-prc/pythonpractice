# https://www.acmicpc.net/problem/1546

n = int(input())
scores = list(map(int, input().split()))
new_scores = []
m = max(scores)
for i in scores:
    new_scores.append(i/m*100)
avg = sum(new_scores) / len(new_scores)
print(avg)