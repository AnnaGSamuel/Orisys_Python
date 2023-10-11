def sum(a,b):
    return a+b
def difference(a,b):
    return a-b
def product(a,b):
    return a*b
def quotient(a,b):
    return a/b
def remainder(a,b):
    return a%b
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
choice = input("Enter choice of operation(+,-,*,/,%): ")

if(choice=="+"):
    print(f"{num1} + {num2} = {sum(num1,num2)}")
elif(choice=="-"):
    print(f"{num1} - {num2} = {difference(num1,num2)}")
elif(choice=="*"):
    print(f"{num1} x {num2} = {product(num1,num2)}")
elif(choice=="/"):
    print(f"{num1} / {num2} = {quotient(num1,num2)}")
elif(choice=="%"):
    print(f"{num1} % {num2} = {remainder(num1,num2)}")
