import re
text = """Elon musk's phone number is 9991116666,
call him if you have any questions on dodgecoin.
Tesla's revenue is 40 billion.
Tesla's CFO number (999)-333-7777.""" # multiple line string

'''pattern = "\d{10}"
print(re.findall(pattern,text)) '''
pattern = re.compile("\d{10}")
print(pattern.match(text))
print(pattern.findall(text))