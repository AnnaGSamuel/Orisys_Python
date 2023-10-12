'''Calculator using Classes and objects'''
class Calculator:
    def __init__(self,n1,n2):
        self.a = n1
        self.b = n2
    def sum(self):
        return self.a+self.b
    def difference(self):
        return self.a-self.b
    def product(self):
        return self.a*self.b
    def quotient(self):
        return self.a/self.b
    def remainder(self):
        return self.a%self.b     

ch = "yes"
while(ch=="yes"):
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    choice = input("Enter choice of operation(+,-,*,/,%): ")
    calc = Calculator(num1,num2)
    
    if(choice=="+"):
        print(f"{num1} + {num2} = {calc.sum()}")
    elif(choice=="-"):
        if(num1>num2):
            print(f"{num1} - {num2} = {calc.difference()}")
        else:
            print(f"{num2} - {num1} = {abs(calc.difference())}")
    elif(choice=="*"):
        print(f"{num1} * {num2} = {calc.product()}")
    elif(choice=="/"):
        print(f"{num1} / {num2} = {calc.quotient()}")
    elif(choice=="%"):
        print(f"{num1} % {num2} = {calc.remainder()}")
    
    ch = input("Do you want to continue? ")
