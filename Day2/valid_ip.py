import re
ip = input("Enter IP address : ")
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

if(re.match(pattern,ip)):
    print("Valid IPv4 address.")
else:
    print("Invalid IPv4 address.")