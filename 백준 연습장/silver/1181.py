# https://www.acmicpc.net/problem/1181
amount = int(input())
word_list = set()
for i in range(amount):
    word_list.add(input())

word_list = list(word_list)

word_list.sort()
word_list.sort(key=len)

for word in word_list: # print(*word_list)로 사용 가능
    print(word)

