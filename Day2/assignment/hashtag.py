import re
text = """Elon musk's phone number is 9991116666,
call him if you have any questions on dodgecoin.
Tesla's revenue is 40 billion.
Tesla's CFO number (999)-333-7777.
#halloween gww6677sj #horror """

pattern = "#\w*"
print(re.findall(pattern,text)) 