
# # 간단한 if문
# x = 5
# if x > 3:
#     print("x는 3보다 큽니다.")
#
# # if else
# age = 18
# if age >= 18:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")
#
# # 중첩된 if else
# score = 85
# if score >= 90:
#     print("A 등급")
# else:
#     if score >= 80:
#         print("B 등급")
#     else:
#         if score >= 70:
#             print("C 등급")
#         else:
#             print("D 등급")
#
# # if elif
# marks = 75
# if marks >= 90:
#     print("A등급")
# elif marks >= 80:
#     print("B등급")
# elif marks >= 70:
#     print("C등급")
# else:
#     print("D등급")
#
# # 입력 if
# a = int(input("Enter Number Greater then or equal to 2: "))
# if a >= 2:
#     print("Correct! You have Entered :", a)
# else:
#     print("Wrong! You have Entered :", a)
#
# #input에 대한 조건문 else
# day = input("요일을 입력하세요: ")
# if day == "Mon":
#     print("월요일")
# elif day == "Tue":
#     print("화요일")
# elif day == "Wed":
#     print("수요일")
# else:
#     print("휴일")
#
# # while문
# i = int(input("Enter Number :"))
# while i < 10:
#     i += 1
#     print("i: ", i)
# else:
#     print("else")
#
# # 끝나지 않는 while문
# while True:
#     a = int(input("Enter Menu Number: "))
#     if a == 0:
#         break
#     print("a: ", a)
#
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
# print("코드 종료")
#
# a = 2
# while a <= 20:
#     print(a)
#     a += 2
# print("코드 종료")
#
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
# else: print("While 조건이 거짓이므로 Else 부분 실행됨")
# print("코드 종료")
#
# # # 무한 루프
# # while True:
# #     print("안녕하세요")
# # print("코드 종료")
#
# i = 0
# while True:
#     i += 1
#     print(i)
#     if i == 5:
#         break
# print("코드 종료")
#
# # 중첩
# i = 1
# while i <= 3:
#     print("Outer Loop", i)
#     i += 1
#     j = 1
#     while j <= 5:
#         print("Inner Loop", j)
#         j += 1
# print("코드 종료")
#
# # range()
#
# for i in range(5):
#     print(i)
#
# for i in range(2,7):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)
#
# for i in range(-1, -10, -2):
#     print(i)
#
# a = range(5)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
#
# print("Reverse Rage with Start, stop, step")
# r = range(5, 0 ,-1)
# print(r[0])
# print(r[1])
# print(r[2])
# print(r[3])
# print(r[4])
#
# # for in
# st = "멋쟁이 사자"
# for ch in st:
#     print(ch)
# else:
#     print("Else")
# print("코드 종료")
#
# # pass 문
# a = 5
# if a < 6:
#     pass
# else:
#     print("6보다 큼")
#
# # 배열 생성 및 원소 접근
#
# import array
# stu_roll = array.array('i', [101,102,103,104,105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])
#
# print("for in 사용")
# for element in stu_roll:
#     print(element)
#
# print("인덱스를 이용한 순회")
# n = len(stu_roll)
# for i in range(n):
#     print(i, '=', stu_roll)
#
# print("인덱스를 사용한 while 루프 배열 순회")
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1

# 배열에 삽입

import array
stu_roll = array.array('i', [101,102,103,104,105])

n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("Array After Insert")
stu_roll.insert(1, 106)
stu_roll.insert(3, 107)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1