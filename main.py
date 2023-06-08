# def pw(x, y):
#     z = x ** y
#     print(z)
#
#
# pw(2, 5)
# pw(y=5, x=2)
#
#
# # pw(5, 2, 3) 매개변수를 2개까지 받을 수 있는데 3개를 줘서 오류가 발생
#
# def show(name, age=30):
#     print(f"Name: {name} Age: {age}")
#
#
# # 키워드 인자는 순서가 바뀌어도 실행 결과가 같음
# show(name="황주원", age=27)
# show(age=27, name="황주원")
#
#
# # 기본 인수를 사용하면 값이 주어지지 않았을 때 기본으로 사용하는 값이 설정됨
# def show(name, age=27):
#     print(f"Name: {name} Age: {age}")
#
#
# show(name="황주원")
#
# # 가변 인자 길이 실습
# def add(x, y):
#     z = x + y
#     print("Addition: ", z)
#
#
# add(5, 2)
#
#
# def add(*num):
#     z = num[0] + num[1] + num[2]
#     print("Addition *: ", z)
#
#
# add(5, 2, 4)
#
#
# def add(x, *num):
#     z = x + num[0] + num[1]
#     print("Addition x  *: ", z)
#
#
# add(5, 2, 4)
#
#
# # 가변 키워드 인자
# def add(**num):
#     z = num['a'] + num['b'] + num['c']
#     print('Addition: ', z)
#
#
# add(a=5, b=2, c=4, d=5)
#
# # 지역변수와 전역변수
#
# def show():
#     x = 10
#     print(x)
#
#
# show()
#
#
# def add(y):
#     x = 10
#     print(x + y)
#
#
# add(20)
#
# a = 50
#
#
# def show():
#     x = 10
#     print(x)  # 지역 변수
#     print(a)  # 전역 변수
#
#
# show()
#
# print("Global Variable a: ", a)
# i = 0
#
#
# def myfun():
#     a = i + 1
#     print("My Function", a)
#
#
# myfun()
# print("Global Variable a: ", a)
#
# i = 1
#
# i += 1
#
# def myfun():
#     b = i + 1
#     print("My function i:", i)
#
# myfun()
#
# # Global 키워드
#
# a = 50
#
# def show():
#     a = 10
#     print("show-A: ", a)
#
# show()
# print("A:", a)
#
# def show2():
#     global a
#     print("show2-A: ", a)
#     a= 20
#     print("show2-A2: ", a)
#
# show2()
# print("A: ", a)
#
# # 리스트 실습
#
# fruits = ["apple", "banana", "cherry", "orange"]
#
# print(fruits)
#
# fruits.append("grape")
#
# print(fruits)
#
# fruits.insert(2, "kiwi")
#
# print(fruits)
#
# print(fruits.pop())
# print(fruits.pop(1))
#
# fruits.append("cherry")
# print(fruits)
#
# print(fruits.index("cherry"))
# print(fruits.remove("cherry"))
# print(fruits.index("cherry"))
# print(fruits.remove("cherry"))
# # print(fruits.index("cherry"))
#
# fruits.reverse()
#
# print(fruits)
#
# # 리스트 연결
#
# fruits = ["apple", "banana", "cherry", "orange"]
# vegetables = ["carrot", "cucumber"]
#
# grocery = fruits + vegetables
# print(grocery)
#
# # 리스트 정렬
#
# numbers = [10, 5, 8, 1, 7]
# numbers.sort()
# print(numbers)
#
# slice_numbers = numbers[1:4]
#
# print(slice_numbers)
#
# numbers_copy = numbers.copy()
# print(numbers_copy)
#
# numbers_clone = numbers[:]
# print(numbers_clone)
#
# # 사용자 입력으로 리스트 만들기
#
# user_input_list = []
# num_elements = int(input("Enter Number of Element: "))
# for i in range(num_elements):
#     user_input_list.append(input("Enter Element:"))
#
# print("User Input List:")
# for element in user_input_list:
#     print(element)
#
# print(user_input_list)
#
# # 제네레이터 실습
#
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# runner = fibonacci(10)
#
# print(next(runner))
#
# print("======")
# print(runner)
# print(next(runner))
# print("======")
#
# for num in runner:
#     print(num)
#
# # 알파넷 제네레이터
#
# def generate_alphabet(start_letter, end_letter):
#     start = ord(start_letter)
#     end = ord(end_letter)
#     while start <= end:
#         yield chr(start)
#         start += 1
#
# runner = generate_alphabet("A", "F")
#
# for letter in runner:
#     print(letter)
#
# # 튜플
#
# b = (10)
# c = (10,)
#
# print(b)
# print(c)
#
# d = (10, 20, 30, 40)
# e = (10, 20, -50, 21.3, '안녕하세요')
# f = 10, 20, -50, 21.3, '안녕하세요'
#
# print(d, e, f, sep='\n')
#
# print(f[1])
# print(f[2])
# print(f[3])
# print(f[4])
#
# print(f[:3])
# print(f[-2:])
#
# print(f[1:4])
# print(f[3:])
# print(c + f)
# print(f * 5)
# print(10 in f)
# print("========")
# h = (10, 20, -50, 20)
# print(min(h), max(h))
# print(h.count(20))
# print(h.index(20))
# sorted_a = sorted(h)
# print(sorted_a)
# # 튜플 언패킹
# a = (10, 20, -50)
# x, y, z = a
# print(x, y, z)
#
# a = 1
# b = 2
#
# temp = a
# a = b
# b = temp
# print(a, b)
#
# a, b = b, a
# print(a, b)
#
# print(list(h), type(list(h)))
# print(tuple(list(h)), type(tuple(list(h))))
#
# nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# 셋 실습
a = {10, 20, 30}
a = {10, 20, 30, "멋쟁이사자", "Hi", 40}
a = {10, 20, 30, "멋쟁이사자", "Hi", 40, 10, 20}

new_set = a.copy()

b = set()
print(type(b))
a.add(50)
a.update([10, 20, 60, 70])
print(a)
a.remove("멋쟁이사자")
a.discard("멋쟁이사자")
a.discard(70)
print(a)

# 셋 초기화

# new_set.clear()
# print(new_set)

# 교집합과 합집합, 차집합, 부분집합, 대칭차집합
intersection_a_new = a.intersection(new_set)

print(intersection_a_new)

union_a = a.union(new_set)
print('union_a:', union_a)

difference_a = a.difference(new_set)
print('difference_a', difference_a)

print(b.issubset(a))
print(a.issuperset(b))

sym_a = a.symmetric_difference(new_set)
print('symmetric_difference:', sym_a)