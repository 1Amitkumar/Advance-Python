import re
s = "regular expression example"
match = re.match(r're', s)
if match:
    print(match.group())