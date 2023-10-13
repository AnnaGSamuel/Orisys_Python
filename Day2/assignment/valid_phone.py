'''check country code '''
import re

phone_no = input("Enter phone number : ")
pattern = "\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\)-\d{3}-\d{4}|\(\d{3}\)\s\d{3}-\d{4}"
if(re.match(pattern,phone_no)):
    print("Phone number is valid")
else:
    print("Invalid phone number")