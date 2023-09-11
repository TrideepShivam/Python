class Employee:
    def __init__(self,name,e_no,role,salary):
        self.name = name
        self.e_no=e_no
        self.role=role
        self.salary = salary
    def printF(self):
        print(self.name,self.e_no,self.role,self.salary)

e=Employee("ajith",1,"senior",200000)
e.printF()
