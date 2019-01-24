import re
val = "Ravi email is ravi@xyzhost.com"
match = re.search('([\w.-]+)@([\w.-]+)', val)
if match:
    print(match.group())   # ravi@xyzhost.com (whole match)
    print(match.group(1))  # ravi (username, group 1)
    print(match.group(2))  # xyzhost (host, group 2)