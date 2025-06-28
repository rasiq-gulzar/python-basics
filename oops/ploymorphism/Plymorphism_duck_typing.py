# Different classes with the same method name
class Duck:
    def speak(self):
        return "Quack quack!"

class Dog:
    def speak(self):
        return "Woof woof!"

class Cat:
    def speak(self):
        return "Meow meow!"

# Function that demonstrates duck typing
def make_animal_speak(animal):
    print(animal.speak())

# Creating objects
donald = Duck()
rover = Dog()
whiskers = Cat()

# Same function works with different objects
make_animal_speak(donald)    # Output: Quack quack!
make_animal_speak(rover)     # Output: Woof woof!
make_animal_speak(whiskers)  # Output: Meow meow!