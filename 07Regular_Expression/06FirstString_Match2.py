import re
s = "end of regular expression"
match = re.search(r'^e', s)
if match:
    print(match.group())