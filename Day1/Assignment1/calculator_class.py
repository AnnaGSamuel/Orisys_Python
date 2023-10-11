'''Calculator using Classes and objects'''
class Calculator:
    def sum(self,a,b):
        return a+b
    def difference(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def quotient(self,a,b):
        return a/b
    def remainder(self,a,b):
        return a%b     

ch = "yes"
while(ch=="yes"):
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    choice = input("Enter choice of operation(+,-,*,/,%): ")
    calc = Calculator()
    
    if(choice=="+"):
        print(f"{num1} + {num2} = {calc.sum(num1,num2)}")
    elif(choice=="-"):
        if(num1>num2):
            print(f"{num1} - {num2} = {calc.difference(num1,num2)}")
        else:
            print(f"{num2} - {num1} = {calc.difference(num2,num1)}")
    elif(choice=="*"):
        print(f"{num1} * {num2} = {calc.product(num1,num2)}")
    elif(choice=="/"):
        print(f"{num1} / {num2} = {calc.quotient(num1,num2)}")
    elif(choice=="%"):
        print(f"{num1} % {num2} = {calc.remainder(num1,num2)}")
    
    ch = input("Do you want to continue? ")
