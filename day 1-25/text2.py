import re

pattern = re.compile(r"(\w+)\s+\d{3}-\d{8}")

with open ("text",'r') as file:
    for line in file:
        match = pattern.search(line)
        if match:
            print(match.group(1))

