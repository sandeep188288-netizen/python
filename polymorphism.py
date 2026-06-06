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
'''class Animal:
    name = "lion"
    def speak(self):
        print("hello I roar")

class Human(Animal):
    name = "sandeep "

    def speak(self):
        super().speak()
        print("hello my name is akarsh")

obj = Human()
obj.speak()'''

# ---------------------------------------------
'''
# encapsulation
#we use access modifiers
class Animal:
    a = 12      #public attribute
    _b = 23     #protected attribute
    __c = 34    #private attribute

    def hello(self): #public method
        print("how are you")

    def hello2(self): #protected method
        print("hello i am protected method")

    @classmethod 
    def __hello3(self): #private method
        print("hello i am private method")

obj = Animal()
print(obj.a)
'''

# ---------------------------------------------

# abstraction

from abc import ABC, abstractmethod

class person(ABC):
    @abstractmethod
    def info():
        pass

    @abstractmethod
    def register():
        pass


class Teacher(person):
    def info():
        pass

    def register():
        pass

class Student(person):
    def info():
        pass

    def register():
        pass
    
obj = Teacher()