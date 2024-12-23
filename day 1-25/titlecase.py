def func(fname, lname):
    name = fname + " " + lname
    name = name.title()
    return name


formattedname = func(input("Enter your first name: "), input("Enter your last name: "))

print("Formatted name = ", formattedname)