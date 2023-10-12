import re

date = input("Enter a date : ")
pattern = r"0?[1-9]|1[0-2]/0?[1-9]/\d{4}"

print(re.findall(pattern,date))