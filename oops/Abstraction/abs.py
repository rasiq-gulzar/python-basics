# # # what is abstraction in python?
# # # # Abstraction is the concept of hiding the real implementation of an application from the user and 
# # # # emphasizing only on usage of it. For example, consider your phone, you just need to know how to use it and 
# # # # what services it provides, you don’t need to know how it works. That’s what abstraction is.

# # # #we need to be carefull about three things: 
# # # 1. Abstract class(using abc)
# # # 2.Abstract method(using abc)
# # # example:
# # from abc import ABC, abstractmethod
# # # class Animal(ABC):
# # #     @abstractmethod
# # #     def move(self):
# # #         pass
# # #     @abstractmethod
# # #     def move(self):
# # #         pass
# # # # this is called abstract base class
# # # # import abc  
# # # # print(dir(abc)) #this is used to check the methods of abc module


# # class Animal(ABC):
# #     @abstractmethod
# #     def move(self):
# #         pass
# #     @abstractmethod
# #     def sound(self):
# #         pass

# # class Dog(Animal):
# #     def move(self):
# #         return "Dog runs"
# #     def sound(self):
# #         return "Dog barks"
    
# # class Cat(Animal):
# #     def move(self):
# #         return "Cat runs"
# #     def sound(self):
# #         return "Cat meows"

# # d = Dog()
# # cat= Cat()
# # print(d.move())
# # print(cat.move())
# # print(d.sound())
# # print(cat.sound())

# # # Simple example of abstraction with a Shape class

# # # class Shape(ABC):
# # #     @abstractmethod
# # #     def area(self):
# # #         pass

# # # class Square(Shape):
# # #     def __init__(self, side):
# # #         self.side = side
    
# # #     def area(self):
# # #         return self.side * self.side

# # # # Create and use a Square
# # # square = Square(5)
# # # print(f"Area of square: {square.area()}")  # Output: Area of square: 25


# list1=[1212,3232,4242]
# press=int(input('enter the number to check it '))
# for i in list1:
#     if press==i:
#         print('found')
#     else:
#         print('not found')

for i in range(3):
    print(i)
else:
    print('done')