class calculator:
    def __init__(self,a):
        print("welcome to the calculator")
        self.a=a
    @staticmethod
    def square(a):
        print("the suqare of the number is ", a*a)
    def cube(self):
        print(f"cube of the number is {self.a*self.a*self.a}")    
    def squareroot(self):
        print("sqroot of the number is",self.a**(1/2))
a=float(input("enter the number"))
b=calculator(a)
b.cube()
b.square(a)
b.squareroot()

#or
"""
class Calculator:
    def __init__(self, n):#we are passing n here so it automatically becomees part of the object
                          #or else we would have to define it indivisullay with other function
        self.n = n 
    
    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()
"""
#to use both class and object attribute if needed
"""
class Calculator:
    def __init__(self, a):
        print("Welcome to the calculator")
        self.a = a
        self.cube = None  # Optional: define upfront

    def cube_method(self):
        return self.a ** 3

    def get_cube(self):
        # Use attribute if set, else fallback to method
        if self.cube is not None:
            print(f"Cube from attribute: {self.cube}")
        else:
            print(f"Cube from method: {self.cube_method()}")
a = float(input("Enter the number: "))
calc = Calculator(a)

# Case 1: No attribute set, use method
calc.get_cube()

# Case 2: Set attribute, it overrides method
calc.cube = 6
calc.get_cube()
"""
        
    