import re

s = "Ravi's mobile numbers are 12345-54321 and 67891-19876"
match = re.findall(r'\d{5}', s)

if match:
    print(match)