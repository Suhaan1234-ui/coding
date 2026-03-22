class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):#this is a dunder method
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)#using thid without operator overloading will show an error as it is not defined for the class Number,
#every time we use + operator it will call the __add__ method and pass the second number as an argument to it, and it will return the sum of the two numbers.
#every operator has a corresponding method that can be overloaded to define custom behavior for that operator when used with instances of a class.
#everything in python is a class and every operator is a method that can be overloaded to define custom behavior for that operator when used with instances of a class.