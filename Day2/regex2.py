import re
import content

print("Text : ",content.text)

pattern = re.compile("\d{10}")
print(pattern.findall(content.text))

