string = input("ENter a string: ")

vowels = ['a','e','i','o','u']

new = []

for s in string:
    if s not in vowels:
        new.append(s)

for i in new:
    print(i, end = "")