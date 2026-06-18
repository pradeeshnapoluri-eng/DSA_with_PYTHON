class Company:
    def __init__(self,name,employees,laptops):
        self.name=name
        self.employees=100
        self.laptops=90

    def workers(self,job_role):
        self.job_role=job_role
        print(f"{self.name} job role is {self.job_role}")

    def income(self,salary):
        self.monthly_salary=salary
        print(f"salary is {salary}")
class MNC:
    def bigcompany(self,products,sales):
        print("f")
# total=Company("keerthi","python developer","lenova laptop")
# print(total.name)
# print(total.employees)
# total.income(125000)
# total.workers("python developer")