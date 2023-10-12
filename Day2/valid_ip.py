import re
ip = input("Enter IP address : ")
pattern = "25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]\.25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]\.25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]\.25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]"

if(re.match(pattern,ip)):
    print("Valid IPv4 address.")
else:
    print("Invalid IPv4 address.")