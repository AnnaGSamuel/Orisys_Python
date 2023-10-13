'''Validate email'''
import re

email = input("Enter email : ")
pattern = "\w*@(?!yahoo|hotmail)\w*\.com|\w*@(?!yahoo|hotmail)\w*\.in|\w*@(?!yahoo|hotmail)\w*\.org"
if(re.match(pattern,email)):
    print("Email is valid")
else:
    print("Invalid email")