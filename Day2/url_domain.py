import re

url = input("Enter a URL : ")
pattern = re.compile(r"https?://(www\.)?([a-zA-Z0-9.-]+\b)") 

print("Domain : ", pattern.match(url).group(2))
