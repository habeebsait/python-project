def add(n,m):
    return n+m

def sub(n,m):
    return n-m

def mul(n,m):
    return n*m

def divi(n,m):
    return n/m


operations = {

    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : divi
}

lst = []

for i in operations:
    print(i)

num1 = float(input("Enter your first number: "))
lst.append(num1)

operator = input("Enter your operator: ")

lst.append(operator)

num2 = float(input("Enter your second number: "))
lst.append(num2)


result = operations[operator](num1,num2)
print(result)



while True:
    con = input("Do u want to calculate more to it? (y/n): ").lower()

    if con == "y":
        op = input("Enter your operator: ")
        lst.append(op)
        num = float(input("Enter your number: "))
        lst.append(num)
        
        result = operations[op](result, num)
        print(result)
        
        
    elif con == "n":
        print("GoodBye!")
        break

    else:
        print("Invalid operator! Retry!")

lst.append("=")
lst.append(result)

for i in lst:
    print(i , end = " ")
