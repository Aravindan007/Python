class Employee:
    def input_data(self):
        self.emp_name=input()
        self.emp_id=int(input())
        self.designation=input()
        self.salary=int(input())
    def allocate(self):
        if(self.salary>25000):
            self.designation='A-level'
        elif(self.salary==25000 and self.salary<=20000):
            self.designation='B-level'
        elif(self.salary>=20000 and self.salary<=15000):
            self.designation='c-level'
        else:
            self.designation='D-level'
    def show(self):
        print(self.designation)
s=Employee()
s.input_data()
s.allocate()
s.show()
print(Employee.show)
        
