# def greeting():         #defining a functon 
#     print("hello good morning !! ")

# greeting()           #calling a function

# ------------------------------------------------------

# def addition(a,b):   #a and b are parameters
#     print(a+b)

# addition(10,20)

# ------------------------------------------------------

# def pallindrome(n):
#     rev = 0
#     copy = n
    
#     while n != 0:
#         rev = rev*10 + n%10
#         n = n // 10

#     if rev == copy:
#         print("pallindrome")

#     else:
#         print("not a pallindrome")

# pallindrome(121)


## ------------------------------------------------------
#1) POSITIONAL ARGUMENTS

# def multiply(a,b):      #fixed position
#     print(a*b)

# multiply(3,4)           #fixed positional arguments


#2)DEFAULT ARGUMENTS

# def info(name,age):
#     print(f"your name is {name} and your age is {age}")

# info(age = 20, name = "sandeep")

# def info(a,b,c,d,e):
#     print(a,b,c,d,e)
# info(12,34,e = 67, c = 12, d = 67)

#if u give a value using default argument you always
# have to give further value ussing defaul targument

# ------------------------------------------------------

# def info(name,age,id = None):
#     print("info recieved")

# info("sandeep", 20) 

# ------------------------------------------------------(STRONG NUMBER)

def strongnumber(n):
    copy = n
    total = 0

    while n > 0:
        digit = n % 10

        fact = 1
        for i in range(1, digit + 1):
            fact *= i

        total += fact
        n = n // 10

    if total == copy:
        print("Strong Number!")
    else:
        print("Not a Strong Number!")

strongnumber(145) 

# ------------------------------------------------------

#RETURN VS PRINT

# def hello():
#     return "how are you"

# a = hello()
# print(a)
# # print(hello()) #or

# ------------------------------------------------------


# def agechecker(n):
#     if n >= 18:
#         return True
#     else:
#         return False

# age = int(input("tell your age: "))

# if agechecker(age):
#     print("you can vote ")

# else:
#     print("you cannot vote ")

# ------------------------------------------------------

# def hello1():
#     hello2()
#     print("hello 1")

# def hello2():
#     hello3()
#     print("hello 2")

# def hello3():
#     hello4()
#     print("hello 3")

# def hello1():
#     print("hello 4")

# hello1()

# ------------------------------------------------------
#recursive calls
# def numbers(n):
#     if n == 101:
#         return "done"
#     numbers(n+1)
#     print(n)
    

# numbers(1)

# ------------------------------------------------------
