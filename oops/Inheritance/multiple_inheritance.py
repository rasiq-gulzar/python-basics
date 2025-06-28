#in mulitple inheritance the child inherits the properties of multiple parent classes
# syntax class parent1:
#     pass
# class parent2:
#     pass
# class child(parent1,parent2):
    # pass
    
    
#example:
# class Animal:
#     def __init__(self,name):
#         self.name=name
        
#     def speak(self):
#         print(f'{self.name} makes sound')
        
# class Bird:
#     def __init__(self,wings):
#         self.wings=wings
        
#     def fly(self):
#         print(f'{self.wings} wings')

# class sparrow(Bird,Animal):
#     def __init__(self,name,wings):
#         Animal.__init__(self,name)
#         Bird.__init__(self,wings)
#     def display(self):
#         print(f'{self.name} has {self.wings} wings')
        
# brid=sparrow('sparrow',2)
# brid.speak()
# brid.fly()
# brid.display()
# # print(brid.name)
# # print(brid.wings)

# #in python when the child inherrits the properties of multiple classes it follow the MRO: method resolution order
# # MRO is the order in which the classes are inherited by the child class in case of multiple inheritance in python.
# # MRO is calculated using C3 linearization algorithm.
# # C3 linearization algorithm is used to maintain the order of inheritance in the child class. 

# #to check the mro:
# print(sparrow.mro())

#method overriding the child class can override the methods of the parent class in multiple inheritance
class Animal:
    def speak(self):
        print('Animals can speak')
class Bird:
    def speak(self):
        print('Birds can speak')
        
class sparrow(Animal,Bird):
    def speak(self):
        Animal.speak(self)
        Bird.speak(self)
        
sparrow1=sparrow()
sparrow1.speak()
print(sparrow.mro())


        

