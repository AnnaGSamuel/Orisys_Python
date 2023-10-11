def calculate(num1,num2,ch):
    if(ch=="+"):
        print(f"{num1} + {num2} = {num1+num2}")
    elif(ch=="-"):
        if(num1>num2):
            print(f"{num1} - {num2} = {num1-num2}")
        else:
            print(f"{num2} - {num1} = {num2-num1}")
    elif(ch=="*"):
        print(f"{num1} * {num2} = {num1*num2}")
    elif(ch=="/"):
        print(f"{num1} / {num2} = {num1/num2}")
    elif(ch=="%"):
        print(f"{num1} % {num2} = {num1%num2}")
        
ch = "yes"
while(ch=="yes"):
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    choice = input("Enter choice of operation(+,-,*,/,%): ")
    calculate(num1,num2,choice)
    ch = input("Do you want to continue? ")