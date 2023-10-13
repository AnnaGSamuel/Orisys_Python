import re

text = input("Enter a text : ")
pattern = r""

final_text = re.sub(r'<.*?>', '', text)

print(final_text)