class programer:
    company="microsoft"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def show(self):
        print(self.name,self.age,self.salary)
suhaan=programer("suhaan",20,5000000)
suhaan.show()
