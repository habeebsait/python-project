calc_art = '''
 _____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(calc_art)


def add(a,b):
    return a+b

def sub(a,b):
    return a,b

def multi(a,b):
    return a*b

def divi(a,b):
    return a/b

lst = []

result = int(input("Enter the first number: "))
lst.append(str(result))
op = input("Enter the operator you want to use: (+, -, *, /): ")
lst.append(op)
num2 = int(input("Enter the second number: "))
lst.append(str(num2))


while True:
    if op == "+":
        result += num2

    elif op == "-":
        result -= num2

    elif op == "*":
        result *= num2

    elif op == "/":
        result /= num2

    elif op == "=":
        break

    else:
        print("Wrong operator")
    


    op = input("Enter the operator you want to use: (+, -, *, /, =): ")
    lst.append(op)
    if op == "=":
        break
    num2 =  int(input("Enter the second number: "))
    lst.append(str(num2))

lst.append(result)
print(result)
print("\n\n")
for i in lst:
    print(i, end = "")