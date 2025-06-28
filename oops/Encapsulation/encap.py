class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary #private variable

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary, must be positive")
    
    def display(self):
        print(f"Name: {self.name}, Salary: {self.get_salary()}")
        
class Staff(Employee):
    def __init__(self, name, salary, title):
        super().__init__(name, salary)
        self.title = title

    def display2(self):
        print(f"Name: {self.name}, Salary: {self.get_salary()}, Title: {self.title}")
        
class Staff2(Staff):
    def __init__(self, name, salary, title, dept):
        super().__init__(name, salary, title)
        self.dept = dept

    def display3(self):
        print(f"Name: {self.name}, Salary: {self.get_salary()}, Title: {self.title}, Dept: {self.dept}")
        
        
class Staff3(Employee):
    def __init__(self, name, salary,worker):
        super().__init__(name, salary)
        self.worker = worker

    def display3(self):
        print(f"Name: {self.name}, Salary: {self.get_salary()}, Work: {self.worker}")
        
   
class Final(Staff2,Staff):
    def __init__(self, name, salary, title, dept,coordinator):
        super().__init__(name, salary, title, dept)
        self.coordinator = coordinator

    def display4(self):
        print(f"Name: {self.name}, Salary: {self.get_salary()}, Title: {self.title}, Coordinator: {self.coordinator}")
        
emp=Employee("John", 10000)
# emp.display()
print(emp.get_salary())
emp.set_salary(60000)


staff=Staff("Jane", 20000, "Manager")
staff.display2()

staff2=Staff2("Jill", 30000, "Director", "HR")
staff2.display3()

staff3=Staff3("Jack", 40000, "HR")
staff3.display3()

final=Final("Jill", 30000, "Director", "HR", "John")
final.display4()