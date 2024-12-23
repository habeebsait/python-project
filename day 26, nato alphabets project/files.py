import pandas as pd

f1 = open("day 26/file1.txt")
r1 = f1.readlines()
f2 = open("day 26/file2.txt")
r2 = f2.readlines()


result = [n.strip() for n in r1 if n in r2]

print(result)