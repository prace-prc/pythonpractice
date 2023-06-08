def pw(x, y):
    z = x ** y
    print(z)


pw(2, 5)
pw(y=5, x=2)


# pw(5, 2, 3) 매개변수를 2개까지 받을 수 있는데 3개를 줘서 오류가 발생

def show(name, age=30):
    print(f"Name: {name} Age: {age}")


# 키워드 인자는 순서가 바뀌어도 실행 결과가 같음
show(name="황주원", age=27)
show(age=27, name="황주원")


# 기본 인수를 사용하면 값이 주어지지 않았을 때 기본으로 사용하는 값이 설정됨
def show(name, age=27):
    print(f"Name: {name} Age: {age}")


show(name="황주원")
