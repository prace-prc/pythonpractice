def show():
    x = 10
    print(x)

show()

def add(y):
    x = 10
    print(x)
    print(x+y)

add(20)

a = 50
def show():
    x = 10
    print(x) # local
    print(a) # global

show()

print("Gobal Variable a:", a)
i = 0
def myfun():
    a = i + 1
    print("My Function a:", a)
myfun()
print("Gobal Variable a:", a)
