class Animal:
    def sound(self):
        return "Animal sound"
        
class Dog(Animal):
    def sound(self):
        return "Dog barks"
        
class Cat(Animal):
    def sound(self):
        return "Cat meows"
dog= Dog()
cat= Cat()
print(dog.sound())
print(cat.sound())

#it is also called as runtime polymorphism or overriding

