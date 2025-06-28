#single inheritance: 
#multi inheritace:
#multi-level inheritance:
#hybrid inheritance:

#single inheritance:
# class parent:
#     def properties(self,house,car):
#         self.house=house
#         self.car=car
# class child(parent):
#     def prototype(self,phone):
#         self.phone=phone
# onj=child()
# onj.properties('villa','BMW')
# print(onj.house)

#single inheritance using the constructor
# class parent:
#     def __init__(self,house,car):
#         self.house=house
#         self.car=car
# class child(parent):
#     def __init__(self,house,car,phone):
#         parent.__init__(self,house,car)
# onj=child('villa','BMW','ios')
# print(onj.house)

# class showroom:
#     def items(self,garments,kids,fashion,trend):
#         self.garments=garments
#         self.kids=kids
#         self.fashion=fashion
#         self.trend=trend
        
# class seller(showroom):
#     def temp(self):
#         pass
        
# s1=seller()
# s1.items('pants','shirts','hoddies','jacket')
# print(s1.garments)


#define a class within atturbute name and a method speak create sub class


# #define a class within atturbute name and a method speak create sub class
# class Animal:
#     def speak(self):
#         print('DOG IS BARKING')
        
# class Speak(Animal):
#     def __init__(self):
#         pass

# obj=Speak()
# print(obj.speak())


#create a parent class person sub class employee and self employee id
# class Person:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
# class Employee(Person):
#     def employeId(self,empid):
#         self.empid=empid
        
# obj=Employee()
# obj.details('rasiq',23)
# obj.employeId(123)
# print(f'name is {obj.name} and age is {obj.age} and employee id is {obj.empid}')

#consturctor
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Employee(Person):
#     def __init__(self,name,age,empid):
#         Person.__init__(self,name,age)
#         self.empid=empid
# emp=Employee('rasiq',23,123)
# print(f'name is {emp.name} and age is {emp.age} and employee id is {emp.empid}')


class Showroom:
    def __init__(self,bmw,audi,benz,woxwagon):
        self.bmw=bmw
        self.audi=audi
        self.benz=benz
        self.woxwagon=woxwagon

class Seller1(Showroom):
    def __init__(self,maruti,bmw,audi,benz,wmaroxwagon):
        super().__init__(self,bmw,audi,benz,woxwagon)
        self.maruti=maruti
        
s1=Seller1('maruti','bmw','audi','benz','woxwagon')
print(s1.maruti,s1.bmw,s1.audi,s1.benz,s1.woxwagon)

