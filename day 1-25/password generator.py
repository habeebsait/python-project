#password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

a = input("enter the number of alphabets needed: ")
n = input("Enter the number of numbers needed: ")
s = input("Enter the numbers of symbols needed: ")

for char in range(1,int(a)+1):
    randomchar = random.choice(letters)
    password += randomchar

for char in range(1,int(n)+1):
    randomchar = random.choice(numbers)
    password += randomchar

for char in range(1,int(s)+1):
    randomchar = random.choice(symbols)
    password += randomchar

print(password)
random.shuffle(password)

print(password)

for char in password:
    print(char, end = "")