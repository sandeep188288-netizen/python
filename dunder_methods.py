'''
Dunder/Magic Methods -> it is a special methods in python that define behaviour for built-in operations.
They are prefixed with double underscores(e.g., __init__, __str__).

'''

# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def __str__(self):
#         return f"{self.name} is your name and your marks are {self.marks}"
    
# obj = Students("Sandeep", 95)

# print(obj) 

# ------------------------------------------------------

# class Shopping:
#     def __init__(self, items):
#         self.items = items

#     def __len__(self):
#         return len(self.items)
    
# obj = Shopping(['apple', 'milk', 'bread'])

# obj2 = Shopping(["apple", "bananas"])

# print(len(obj2))

# -----------------------------------------------------

class Numbers:
    def __init__(self, number):
        self.number = number

    def __add__(self, custom):
        return self.number + custom.number
        
obj1 = Numbers(12)
obj2 = Numbers(34)

print(obj1 + obj2)
