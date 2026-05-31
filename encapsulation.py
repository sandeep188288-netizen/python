'''Encapsulation

Access Modifiers
Encapsulation means bundling data (attributes) and
methods into one unit (class).
It also involves controlling access to these attributes
using access modifiers:

: Accessible anywhere. Until Now we were using

Public Attributes and methods.

: Accessible in the class and subclasses.
The protected access modifier in Python
doesn't function as strictly as in some
other languages like Java or C++

: Accessible only in the class.
We use __ (double underscore) to use Private
Attributes and methods Private means PRIVATE
no one can now access these Methods and
Attributes Not even Child classes.'''

class Animal:
    __name = "lion"

    def speak(self):
        print("hello I will roar")


class Human(Animal):
    def say(self):
        print(f"hello my name is {super().__name} ")

obj = Human()

obj.say()