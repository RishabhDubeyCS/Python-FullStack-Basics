class Employee:
    def __init__(self , salary, name , bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_info(self):
        print(f"the name od employee is {self.name}.Salary is {self.salary} .The bond is for {self.bond}years")   

e1 =Employee(4500, "Rishabh",5)
e1.get_info()
        
        