import re

text = input("Enter a text : ")
pattern = r"https?://www\.\S+"

urls = re.findall(pattern,text)

for url in urls:
    print(url)

