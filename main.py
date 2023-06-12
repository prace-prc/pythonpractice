# class Car:
#     # 클래스 속성
#     wheel = 4
#
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#
#     def __str__(self):
#         return f"{self.make}, {self.model}, {self.color}"
#
#     # 메소드
#     def drive(self):
#         return "The car is moving!"
#
#     def stop(self):
#         return "The car has stopped."
#
#
# my_car = Car("Kia", "Morning", "Blue")
#
# # 속성 사용
# print(my_car.make)
#
# # 메소드 호출
# print(my_car.drive())
# print(my_car.stop())

# 상속 실습

# 부모 클래스
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "The engine is running!"


# 자식 클래스
class Car(Vehicle):
    def start_engine(self):
        return super().start_engine() + " It's a car engine."


# 인스턴스 생성
my_car = Car("Toyota", "Corolla", 2020)
# 메소드 호출
print(my_car.start_engine())
