import re


val = "number is 123"
find = re.search(r'\d\d\d', val)
print(find)

print(find.group())