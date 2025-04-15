# class Car:
#     def __init__(self,modelName,modelYear):
#         self.modelName = modelName
#         self.modelYear = modelYear
#     def getModel(self):
#         return str(self.modelYear) + "년식"+self.modelName
#
# car1=Car("Sonata",2002)


#
# class Car:
#     def__init__(self,modelName,modelYear,color,maxSpeed):
#         self.modelName=modelName
#         self.modelYear=modelYear
#         self.color=color
#         self.maxSpeed=maxSpeed
#         self.currentSpeed=0

# class Car:
#     def accelerate(self,speed,second):
#         print(second,"초간 속도를 시속",speed,"(으)로 가속합니다.")
# myCar=Car()
# myCar.accelerate(60,3)

#연습문제 1
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def get_area(self):
#         return self.radius * self.radius
#     def get_perimeter(self):
#         return 2 * 3.14 * self.radius
# myCircle=Circle(10)
# print(myCircle.get_area())
# print(myCircle.get_perimeter())

#연습문제2
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def get_area(self):
#         return self.length * self.width
#     def get_perimeter(self):
#         return (self.length+self.width)*2
# myRectangle = Rectangle(2,3)
# print(myRectangle.get_area())
# print(myRectangle.get_perimeter())

#연습문제3
# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def get_age(self):
#         print(self.age)
#     def get_old(self):
#         self.age+=1
#     def change_name(self,new_name):
#         self.name = new_name

# #연습문제4
# class Car:
#     def __init__(self,model,color,fuel,driver):
#         self.model = model
#         self.color = color
#         self.fuel = fuel
#         self.driver = driver
#     def getFuel(self):
#         return self.fuel
#     def move(self):
#         return self.fuel-=1
#     def getDriver(self):
#         return self.driver
#
# #연습문제5
# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
#     def sub(self):
#         return self.a-self.b
#     def mul(self):
#         return self.a*self.b
#     def div(self):
#         return self.a/self.b




#클래스 변수
# class Person:
#     population = 0
#     def __init_(self,name):
#         self.name = name
#         Person.population +=1

# class Person:
#     def __init__(self,name):
#         self.name = name
# class Car:
#     def __init__(self, modelName, driver):
#         self.modelName = modelName
#         self.driver = driver
#
# p1 = Person("Tony")
# c1 = Car("Sonata",p1)
#
#연습문제 1
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def get_name(self):
#         return self.name
#     def get_old(self):
#         self.age+=1
#     def get_age(self):
#         return self.age
#
# class School:
#     def __init__(self,name,location,students):
#         self.name = name
#         self.location = location
#         self.students = students
#     def change_student(self, s, n):
#         self.students[n]=s
#     def get_location(self):
#         return self.location
#     def get_student_list(self):
#         for i in self.students:
#             print(i.get_name())
#
# Student1=Student("Tony",22)
# Student2=Student("Jane",25)
# Student3=Student("Mary",28)
# Student4=Student("Jack",30)
# Student5=Student("Paul",32)
# student_li=[Student1,Student2,Student3,Student4,Student5]
#
# School1=School("Johns","Seoul",student_li)
# new=Student("h",8)
# School1.change_student(new,0)
# School1.get_student_list()



class Coffee:
    def __init__(self,name,price,hotOrCold,capacity):
        self.name = name
        self.price = price
        self.hotOrCold = hotOrCold
        self.capacity = capacity
    def print(self):
        print(self.name,self.price,self.hotOrCold,self.capacity)
    def drink(self,amount):
        if self.capacity >= amount:
            self.capacity-=amount
    def getPrice(self):
        return self.price
    def getName(self):
        return self.name

class Customer:
    def __init__(self,money,ownCoffee):
        self.money = money
        self.ownCoffee = ownCoffee
    def buyProduct(self,Coffee):
        if self.money-Coffee.price >=0:
            self.ownCoffee = Coffee
            self.money -= Coffee.price
            print(self.ownCoffee.name+"를(을) 구매하였습니다."+" 남은 돈: ",self.money)
        else:
            print('구매x')
    def eatProduct(self,amount):
        if self.ownCoffee:
            self.ownCoffee.drink(amount)
            print(self.ownCoffee.name + "를(을) ", amount, "만큼 마셨습니다.", "남은 용량: ", self.ownCoffee.capacity)
        else:
            print("커피가 없습니다.")


Coffee1 = Coffee("아메리카노",1700,"C",250)
Coffee2 = Coffee("카페라떼", 2100, "H", 250)
Coffee3 = Coffee("카페모카", 2300, "H", 250)
Coffee4 = Coffee("카라멜마끼야또", 2300, "C", 250)
Coffee_li=[Coffee1,Coffee2,Coffee3,Coffee4]

Customer1 = Customer(10000,'아메리카노')
while True:
    num = int(input('1. 구매 2. 섭취 3. 종료'))
    if num == 1 :
        for i in Coffee_li:
            i.print()
        item=int(input())
        Customer1.buyProduct(Coffee_li[item-1])
    elif num == 2 :
        Customer1.eatProduct(50)
    else:
        break







