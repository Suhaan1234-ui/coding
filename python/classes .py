class form:
    name="Suhaan"
    age="17"
    grade="11th" #class attributes
    
    def intro(self):
# if no argument passed,TypeError: form.intro() takes 0 positional arguments but 1 was given
        print(f"hi there its {self.name} and i am {self.age} years old")
arnav=form()
arnav.grade="12th"#object/instance attributes
print(arnav.name,arnav.age,arnav.grade) #instance attributes take priority over class attributes
arnav.intro()  #is equals to form.intro(arnav), thats why argument needed
