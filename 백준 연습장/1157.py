#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

word = input()
word = list(word.upper())
dict = {}

for i in word:
    if i.isalpha():
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

max_count = max(dict.values()) # max_count에 dict에서 가장 많이 나온 글자의 수를 저장함
most_freq = []
for char, count in dict.items(): # dict.items()는 dict의 키밸류 쌍을 반환함. char에는 키가, count에는 밸류가 저장됨.
    if count == max_count:
        most_freq.append(char) # count가 max_count와 같다면 most_freq 리스트에 같았던 키를 저장함 -> 가장 많은 알파벳이 리스트에 저장됨

if len(most_freq) == 1: # 리스트의 길이는 가장 많은 알파벳의 개수와 같음
    print(most_freq[0])
else:
    print('?')

# ChatGPT 코드

# word = input().upper()
# char_count = {}
# max_count = 0
#
# for char in word:
#     if char.isalpha():  # 알파벳인 경우에만 처리
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#         max_count = max(max_count, char_count[char])
#
# most_frequent_chars = [char for char, count in char_count.items() if count == max_count]
#
# if len(most_frequent_chars) == 1:
#     print(most_frequent_chars[0])
# else:
#     print('?')