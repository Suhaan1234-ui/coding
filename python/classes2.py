class form:

    def __init__(self,name,salary,age):
            print("hello")
            self.name=name
            self.salary=salary
            self.age=age
    def intro(self):
         print("aadja;lj")
        
    
    @staticmethod  
    def greet():
        print("good morning") 
arnav=form("suhaa","00000","17")
print(arnav.name,arnav.age,arnav.salary)
arnav.intro() 
arnav.greet()