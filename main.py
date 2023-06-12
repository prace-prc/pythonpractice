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
#
# # 상속 실습
#
# # 부모 클래스
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def start_engine(self):
#         return "The engine is running!"
#
#
# # 자식 클래스
# class Car(Vehicle):
#     def start_engine(self):
#         return super().start_engine() + " It's a car engine."
#
#
# # 인스턴스 생성
# my_car = Car("Toyota", "Corolla", 2020)
# # 메소드 호출
# print(my_car.start_engine())
#
# # 다중 상속 실습
#
# class Engine:
#     def start(self):
#         return "Engine started"
#
#     def stop(self):
#         return "Engine stopped"
#
#
# class Wheels:
#     def rotate(self):
#         return "Wheels are rotating"
#
#
# # 다중 상속
# class Car(Engine, Wheels):
#     pass
#
#
# # 인스턴스 생성
# my_car = Car()
# # 부모 클래스의 메소드 사용
# print(my_car.start())
# print(my_car.rotate())
#
# # 패키지 실습
#
# from MyApp.Handlers.text_handler import handle_text
#
# input_text = "python package practice"
# handle_text(input_text)
#
# # 예외 처리
#
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero")
#
# print("Program continues.")
#
# try:
#     # number = int("Not a number")
#     number = 5 + "Not a number"
# except ValueError:
#     print("Error: Invalid value.")
# except TypeError:
#     print

# 사용자 정의 예외 처리
class CustomExeption(Exception):
    def __init__(self, message):
        self.message = message


try:
    raise CustomExeption("This is a custom exception.")
except CustomExeption as e:
    print(f"Error: {e.message}")
