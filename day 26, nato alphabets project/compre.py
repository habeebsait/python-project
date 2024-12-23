import random

name = ["Habeeb", "Rayyan", "Fardeen"]
random.seed(1)
new = {n:random.randint(1,10) for n in name}
print(new)