# class hello():
#     a = 12
#     def speak(self):
#         print("hello good morning")

# obj = hello()   #created an object
# print(obj.a)    #object can also access class attributes
# obj.speak()     #when we use objects to call any method inside a class
#                 #we always send the location of our object


# class Factory:
#     def __init__(self):
#         print("this is constructor function")   #prints three times

#     print("hello")  # print only once

# a = Factory()
# b = Factory()
# c = Factory() 

# class Factory:
#     def __init__(self, zips, pockets, material):
#         self.zips = zips
#         self.pockets = pockets
#         self.material = material

#     def details(self):
#         print("details of the bag are:")
#         print(f" zips: {self.zips},\n pockets: {self.pockets},\n material: {self.material}")
    

# rebok = Factory(2, 4, "leather")
# campus = Factory(3, 5, "canvas")
# rebok.details()

# -------------------------------------------------------------------

#inheritance 

# singlelevel inheritance -> 1 Parent, 1 Child
'''
class BhopalFactory:

    Reg_num = 123456789


    def __init__(self, color, size, type):
        self.color = color
        self.size = size
        self.type = type

    def details(self):
        print("your shoes details are : ")
        print(self.color)
        print(self.size)
        print(self.type)

class indoreFactory(BhopalFactory):     #single level
    def __init__(self, color, size, type, price):
        super().__init__(color, size, type)     #super() is used to call the parent class constructor -> BhopalFactory
        # BhopalFactory.__init__(self, color, size, type)   #we can also call the parent class constructor
        self.price = price

class UjjainFactory(BhopalFactory):     #multilevlel
    def __init__(self, color, size, type, price, discount):
        super().__init__(color, size, type, price)
        self.discount = discount

shoes1 = BhopalFactory("red", 8, "jordan")

shoe2 = indoreFactory("blue", 9, "sneakers", 5000)

shoe2.details()

'''

'''
class Animal():
    def __inikt__(self, name):
        self.name = name

    def details(self):
        print(self.name)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("hello you can speak")

class Robot(Animal, Human):  
    def __init__(self, name, age):
        super().__init__(name, age)   #calling the parent class constructor


obj = Robot("robot1", 5)
obj.speak()

'''
# -------------------------------------------------------------------

# polymorphism

'''class Animal:
    name = "lion"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("The details are : ")
        print(self.name)
        print(self.age)


class Human:
    name = "sandeep"

    def details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
       
obj1 = Animal("tiger", 3)
obj2 = Human("sandeep", 20)

obj1.details()
obj2.details()

#here both the methods are different but they have same name, this is called polymorphism'''


class BhopalFactory:

    Reg_num = 123456789


    def __init__(self, color, size, type):
        self.color = color
        self.size = size
        self.type = type

    def details(self):
        print("your shoes details are : ")
        print(self.color)
        print(self.size)
        print(self.type)

class indoreFactory(BhopalFactory):     #single level
    def __init__(self, color, size, type, price):
        super().__init__(color, size, type)     
        self.price = price

    def details(self):
        print(super().details())   #calling the parent class method
        print(self.price)

obj = indoreFactory("blue", 9, "sneakers", 5000)
obj.details()

# this obj can now only call one method that is called indorefactory,
# it cannot call bhopalfactory details method and this is called method overriding
