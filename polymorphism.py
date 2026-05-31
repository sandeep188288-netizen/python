'''Polymorphism

Types of polymorphism
Polymorphism allows different classes to define methods
with the same name but different behaviors.
In Python, it is typically achieved through
method overriding.

: Python simulates method
overloading using default
or variable-length arguments,
as it
traditional overloading.

: Occurs when a subclass defines a
method with the same name as its
superclass, replacing the superclass's
method.'''

# class Animal:
#     name = "lion"
#     def speak(self):
#         print("hello I roar")

# class Bird:
#     name = "sparrow"

#     def speak(self):
#         print("hello i tweet")

# obj = Animal()
# obj2 = Bird()

# obj.speak()
# obj2.speak()
# ---------------------------------------------
class Animal:
    name = "lion"
    def speak(self):
        print("hello I roar")

class Human(Animal):
    name = "Akarsh"

    def speak(self):
        super().speak()
        print("hello my name is akarsh")

obj = Human()
obj.speak()