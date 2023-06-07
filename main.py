# # 변수 선언
# a = 10
# b= 3.14
# c = "Hello, World"
# d = [1, 2, 3]
# e = (4, 5, 6)
# f = {7, 8, 9}
# g = {"apple": 1, "banana": 2, "orange": 3}
#
# #데이터 타입 출력
# print("a: ", type(a))
# print("b: ", type(b))
# print("c: ", type(c))
# print("d: ", type(d))
# print("e: ", type(e))
# print("f: ", type(f))
# print("g: ", type(g))
#
# # 덧셈
# a = 4
# b = 2
# total = a + b
# print('total = a + b:', total)
#
# # 뺼셈
# total = a - b
# print('total = a - b:', total)
#
# # 곱셈
# total = a * b
# print('total = a * b:', total)
#
# # 나눗셈
# total = a / b
# print('total = a / b:', total)
#
# a = 5
# b = 2
# print('a % b: ', a % b)
#
# # 거듭제곱
# print('a ** b', a ** b)
#
# # 몫 (양수)
# print(' a // b :', a // b)
#
# # 몫 (음수)
# a = -5
# print('a // b(음수) :', a // b)
#
# # 비교 연산자
# a = 5
# b = 2
# print('a:', a, 'b:', b)
#
# print('a < b: ', a < b)
#
# print('a <= b ', a <= b)
#
# print('a == b ', a == b)
#
# print('a != b ', a != b)
# # 논리 연산자
# a = 5
# b = 2
# c = 3
# d = 200
#
# print('AND 연산자')
# print('a > b and a < c:', a > b and a > c)
#
# print('OR 연산자')
# print('a > b or a < c:', a > b or a < c)
#
# print('NOT 연산자')
# print('not(a < b):', not(a < b))
#
# # 할당 연산자
# a = 10
# b = 20
# m = 15
#
# y = a + b
# print(y)
#
# m += 10 # m = m + 10
# print(m)
#
# m **= 2
# print(m)
#
# m //= 10
# print(m)
#
# #비트 연산자
# a = 10
# b = 15
#
# print('a: ', bin(a))
#
# print('b: ', bin(b))
#
# print('~a =', ~a, bin(~a))
#
# print('a & b: ', a & b)
#
# print('a << 2: ', a << 2)
#
# print('a >> 2: ', bin(a >> 2))
#
# # 멤버 in 연산자
#
# st1 = "Welcome to Home"
# print("to" not in st1)
#
# st2 = "Welcome top Home"
# print("to" not in st2)
#
# st3 = "Welcome to Home"
# print("subs" not in st3)
#
# # is 연산자
#
# a = 10
# b = 10
# print(a is not b)
#
# a = 10
# b = '10'
# print(a is not b)
#
# # 암시적 타입 변환
# a = 5
# b = 2
# print(b, type(b))
# value = a / b
# print(value)
# print(type(value))
#
# x = 10
# y = 5.5
# total = x + y
# print(total)
# print(type(total))
#
# j = "Hello"
# k = "like lion"
# p = j + k
# print(p)
# print(type(p))
#
# q = 20
# u = '10'
# r = q + u # 오류 발생
# print(r)

# 명시적 타입 변환
#
# a = 5
# b = 2
# value = a / b
# print(value, type(value))
# int_value = int(value)
# print(int_value, type(int_value))
#
# q = 20
# u = '10'
# print(type(u))
# r = q + int(u)
# print(r, type(r))
#
# n1 = 10.36
# vn1 = complex(n1)
#
# print(vn1, type(vn1))
#
# n5 = "Kim", "Bae", "Park", "Lee"
# vn5 = list(n5)
#
# print(n5,type(n5))
# print(vn5, type(vn5))
#
# print("1")
# print("2", end='')
# print("3")
# print("4")
#
# data = [10, 20, -50, 21.3, 'LikeLion']
#
# print(data)
#
# print("Like", "Share", "Subscribe", sep='')
# print("Like", "Share", "Subscribe", sep='***')
#
# print("Like", "Share", "Subscribe", sep='***', end='\t')
# print("Like", "Share", "Subscribe", sep='***', end='\n')
#
# m = 40
# print("value: ", m)
#
# name = "황주원"
# age = 27
# print("My name is", name, "and My age is", age)
#
# name = input()
#
# print(name)
#
# name = input("Your Name : ")
# mobile = input("Enter Your Mobile Number : ")
# mb = int(mobile)
# print(mb, type(mb))
#
# price = int(input("Total price : "))
#
# print(price)
# complex_number = complex(input("Enter Complex Number:"))
# print(complex_number)
#
# print("He said, \"Hello World\"")
# print('He said, "Hello World"')
# print('It\'s beautiful day')
# print("It's beautiful day")
#
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

# while문
i = int(input("Enter Number :"))
while i < 10:
    i += 1
    print("i: ", i)
else:
    print("else")

# 끝나지 않는 while문
while True:
    a = int(input("Enter Menu Number: "))
    if a == 0:
        break
    print("a: ", a)

a = 1
while a <= 10:
    print(a)
    a += 1
print("코드 종료")

a = 2
while a <= 20:
    print(a)
    a += 2
print("코드 종료")

a = 1
while a <= 10:
    print(a)
    a += 1
else: print("While 조건이 거짓이므로 Else 부분 실행됨")
print("코드 종료")

# # 무한 루프
# while True:
#     print("안녕하세요")
# print("코드 종료")

i = 0
while True:
    i += 1
    print(i)
    if i == 5:
        break
print("코드 종료")

# 중첩
i = 1
while i <= 3:
    print("Outer Loop", i)
    i += 1
    j = 1
    while j <= 5:
        print("Inner Loop", j)
        j += 1
print("코드 종료")

