import re

def check(passw):
    if len(passw)<6 or len(passw)>12:
        return False
    elif not re.search("[a-z]", passw):
        return False
    elif not re.search("[A-Z]", passw):
        return False
    elif not re.search("[1-9]", passw):
        return False
    elif not re.search("[&#@]", passw):
        return False
    
    return True

passw = input("Enter a pass: ")

if check(passw)== False:
    print("Invalid Password")

else:
    print("Valid password")