class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def newsalary(self):
        return self.salary + (self.increment / 100) * self.salary

    @newsalary.setter
    def newsalary(self, newsalary):
        self.increment = ((newsalary - self.salary) / self.salary) * 100


a = Employee(2000, 12)

print(a.newsalary)   # getter runs here
a.newsalary = 5000   # setter runs here
print(a.increment)
3