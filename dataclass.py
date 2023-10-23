class Project:
    def __innit__(self, name, payment, client):
        self.name= name
        self.payment= payment
        self.client= client

    def __repr__(self):
        return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)}"  
      

class Employee:
    def __innit__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project= project 

p= Project("Django app", 2000, "Globomantics")
e= Employee("Teddy", 22, 1000, p)
print(e.Project)