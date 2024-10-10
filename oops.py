# Inheritance in Python


# Method overriding in Python
class Animal:
    def make_sound(self):
        print("Generic animal sound")

    def legs(self):
        print("They have 4 legs")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")


# Creating objects
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the make_sound method on each object
animal.make_sound()  # Output: Generic animal sound
dog.make_sound()    # Output: Woof!
cat.make_sound()    # Output: Meow!
dog.legs()          # method legs is available in the dog class

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Finally block executed.")