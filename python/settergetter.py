class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property  # Decorator is used to make a method behave like an attribute and is used to get the value of the name attribute this is the getter
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter # Decorator is used to set the value of the name attribute
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Harry Khan" # setter is called here
print(e.fname, e.lname)# getter is called here

e.show()
#setter is used to set the value of the name attribute and getter is used to get the value of the name attribute
# The @property decorator is used to define a method as a property, allowing you to access it like an attribute. The @name.setter decorator is used to define a setter method for the name property, allowing you to set the value of the name attribute. In this example, when you set e.name = "Harry Khan", the setter method is called, which splits the name into first and last names and assigns them to fname and lname attributes. When you access e.fname and e.lname, it retrieves the values set by the setter.
#THEY ARE ALSO USED TO MAKE THE CODE MORE READABLE AND MAINTAINABLE AND ALSO TO IMPLEMENT ENCAPSULATION AND ABSTRACTION IN PYTHON.
# so when e.name is intiralized what happens is that the setter is called and the value of e.name is set to "Harry Khan" and then when we print e.fname and e.lname it prints "Harry" and "Khan" respectively.