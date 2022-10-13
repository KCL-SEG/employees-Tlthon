"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Salary:
    def __str__(self):
        pass

    def __call__(self):
        pass
class MonthlySalary(Salary) :
    def __init__(self, salary:int):
        self.salary = salary

    def __str__(self):
        return f'works on a monthly salary of {self.salary}'
    
    def __call__(self):
        return self.salary
class HourlySalary(Salary) :
    def __init__(self, salary:int , length: int):
        self.salary = salary
        self.length = length

    def __str__(self):
        return f'works on a contract of {self.length} hours at {self.salary}/hour'
    
    def __call__(self):
        return self.salary * self.length

class Commission:
    def __str__(self):
        pass
    def __call__(self):
        pass
class NoCommission(Commission):
    def __init__(self):

        pass
    def __str__(self):
        return f''
    def __call__(self):
        return 0
class BonusCommission(Commission):
    def __init__(self, bonus:int):
        self.bonus = bonus
    def __str__(self):
        return f' and receives a bonus commission of {self.bonus}'
    def __call__(self):
        return self.bonus
class ContractCommission(Commission):
    def __init__(self, amount: int, rate:int):
        self.amount = amount
        self.rate = rate
    def __str__(self):
        return f' and receives a commission for {self.amount} contract(s) at {self.rate}/contract'
    def __call__(self):
        return self.amount * self.rate

class Employee:
    def __init__(self, name, salary:Salary, commission:Commission = NoCommission()):
        self.name = name
        self.salary = salary
        self.commission = commission

    def get_pay(self):
        return self.salary() + self.commission()

    def __str__(self):
        return f'{self.name} {self.salary}{self.commission}. Their total pay is {self.get_pay()}.'

    
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlySalary(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(25, 150), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalary(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlySalary(30, 120), BonusCommission(600))
