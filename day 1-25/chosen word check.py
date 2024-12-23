import random

name = input("Enter a word: ")

blank =""

for i in range(0,len(name)):
    blank += "_"

print(blank)

guess = input("Enter a guess: ")
for i in range(0,len(name)):
    if guess in name[i]:
        print("Yes")

    else:
        print("No")