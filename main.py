import random

a = int(input())
b = int(input())
print(a + b, a - b, a * b, sep='\n')

for i in range(5):
    print('*' * (i + 1))

for i in range(30):
    if i % 10 == 0:
        print()
    print(i + 1, end="\t")

name = {"길동": 20, "철수": 25, "영희": 27}
del (name["길동"])
name["철수"] = 27
print(name)

# amount = int(input('로또를 몇장 구매하시겠습니까? :'))
# for i in range(amount):
#     nums = random.sample(range(1, 46), 6)
#     nums.sort()
#     print(nums)
