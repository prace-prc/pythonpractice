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

# 암시적 타입 변환
a = 5
b = 2
print(b, type(b))
value = a / b
print(value)
print(type(value))

x = 10
y = 5.5
total = x + y
print(total)
print(type(total))

j = "Hello"
k = "like lion"
p = j + k
print(p)
print(type(p))

q = 20
u = '10'
r = q + u # 오류 발생
print(r)