class Employee:
    __slots__=('_name', '_age', '_salary')
    
    def __init__(self, name , age, salary):
        self.name = name
        self.age= age
        self.salary= salary

    def increase_salary (self, percent):
        self.salary += self.salary *(percent/100)

    @property
    def salary (self):
        return self._salary 

    @salary.setter
    def salary (self, salary):
        if salary < 1000:
            raise ValueError ('Minimum wage is $1000')
        self._salary = salary

e = Employee("ji-soo", 38, 1000)
Employee.__dict__["increase_salary"](20)
print(e.salary)                
        
