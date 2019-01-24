import re

val = "Ravi email is ravi@xyzhost.com"
match = re.search(r'[\w.-]+@[\w.-]+', val)

# regular expression will match a email address

if match:
    print(match.group())
else:
    print("match not found")