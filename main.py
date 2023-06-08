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

# 리스트 연결

fruits = ["apple", "banana", "cherry", "orange"]
vegetables = ["carrot", "cucumber"]

grocery = fruits + vegetables
print(grocery)

# 리스트 정렬

numbers = [10, 5, 8, 1, 7]
numbers.sort()
print(numbers)

slice_numbers = numbers[1:4]

print(slice_numbers)

numbers_copy = numbers.copy()
print(numbers_copy)

numbers_clone = numbers[:]
print(numbers_clone)

# 사용자 입력으로 리스트 만들기

user_input_list = []
num_elements = int(input("Enter Number of Element: "))
for i in range(num_elements):
    user_input_list.append(input("Enter Element:"))

print("User Input List:")
for element in user_input_list:
    print(element)

print(user_input_list)