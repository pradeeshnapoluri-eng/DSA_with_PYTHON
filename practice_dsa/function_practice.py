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

class Mnc:
    def __init__(self,app_media,followers):
        self.socialmedia=app_media
        self.strangers=followers
    def bigcompany(self,products,sales):
        self.products=products
        self.trade=sales
        print(f"the company had {self.products} and the sale was {self.trade}")

        
total=Company("keerthi","python developer","lenova laptop")
print(total.name)
print(total.employees)
total.income(125000)
total.workers("python developer")
print()

trading=Mnc("instagram","25k")
print(trading.socialmedia)
##class and func calling ki print dont use
trading.bigcompany("chairs",900)