class Employee:
    def __init__(self, id,name ,desig, age, exp):
        self.id = id
        self.name = name
        self.desig = desig
        self.age = age
        self.experience = exp
    
    
    def add(self):
        id= input("id")
        name = input()
        desig = input()
        age = int(input())
        experience = int(input())

    def display(self):
        print(self.id)
        print(self.name)
        print(self.desig)
        print(self.age)
        print(self.experience)
        
    
    def calculate_salary(self, basic):
        if self.age < 30 and self.experience >= 5:
            final_salary = 1.5 * basic
        elif self.age < 40 and self.experience >= 5:
            final_salary = 1.75 * basic
        elif self.age < 40 and self.experience >= 10:
            final_salary = 2 * basic
        elif self.age < 50 and self.experience >= 20:
            final_salary = 2.25 * basic
        elif self.age < 50 and self.experience >= 25:
            final_salary = 2.5 * basic
        elif self.age < 58 and self.experience >= 30:
            final_salary = 3 * basic
        else:
            final_salary = basic
        return final_salary



emp = Employee("12", "Habeeb", "Software", 35,12)
emp.add()
emp.display()
basic = 2000
print("Salary: ", str(emp.calculate_salary(basic)))