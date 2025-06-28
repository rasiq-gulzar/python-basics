#it is the type of inheritance in which a class is derived from a class which is also derived from another class.
# syntax: 
#     class grandparent:
#         pass
#     class parent(grandparent):
#         pass
#     class child(parent):
#         pass


#example:
# class grandfather:
#     def __init__(self,grandfather_name):
#         self.grandfather_name=grandfather_name
#         #@staticmethod we can write this wihout having the self keyword in the parenthesis
#     def greet(self):
#         print(f'HELLO  I am {self.grandfather_name}, the grandfather of the family')
        
# class father(grandfather):
#     def __init__(self,grandfather_name,age):
#         super().__init__(grandfather_name)
#         self.age=age 
#     def introduce(self):
#         print('I am the father of the family')
#         print(f"i have the age like {self.age}")
       
# class child(father):
#     def __init__(self,grandfather_name,age,child_name):
#         super().__init__(grandfather_name,age)
#         self.child_name=child_name
#     def introduce2(self):
#         print(f'I am the child of the family and my name is {self.child_name}')
               
# obj=child('Dar',48,'rasiq')
# obj.greet()
# obj.introduce()
# obj.introduce2()


