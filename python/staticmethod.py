class form:
    P
    name="Suhaan"
    age="17"
    grade="11th"
    
    def intro(self):
        print(f"hi there its {self.name} and i am {self.age} years old")
    #this function requires the object to be printed 
    @staticmethod  #this is called a decorator used when the fn does not require any ppties of object
    def greet():
        print("good morning")
    #this does not require any need of the object to be passes so we can use static 
arnav=form()
arnav.grade="12th"
print(arnav.name,arnav.age,arnav.grade) 
arnav.intro() 
arnav.greet()