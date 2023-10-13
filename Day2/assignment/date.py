import re

text = input("Enter a text : ")
pattern = re.compile(r"((0?[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/(\d{4}))")

date = pattern.match(text).group(1)
print(date)
