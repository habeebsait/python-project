try:
    age = int(input("Enter age: "))

except Exception as e:
    print(e)
    age = int(input("Age: "))

print("Hello")