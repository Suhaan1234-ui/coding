class form:
    
    name="Suhaan"
    age="17"
    grade="11th"
    def __init__(self):#this is a constructor(__ fns are called dunder methods)
            print("hello")
    def intro(self):
        print(f"hi there its {self.name} and i am {self.age} years old")
    
    @staticmethod  
    def greet():
        print("good morning") 
arnav=form()
arnav.grade="12th"
print(arnav.name,arnav.age,arnav.grade) 
arnav.intro() 
arnav.greet()