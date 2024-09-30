from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_file():
    web= website_entry.get()
    mail = email_entry.get()
    passw = pass_entry.get()
    
    if len(web) ==0 or len(mail)==0 or len(passw) ==0:
        messagebox.showerror(title="Warning!!", message= "Fields are empty")
        fields = False
    
    else:
        warning = messagebox.askokcancel(title="Title", message= f"These are the details entered: \nWebsite: {web}\nEmail: {mail}\nPassword:{passw}\nIs it ok to save?")

    

        if warning == True:
            with open("day 29, password gui/data.txt","a") as f:
                f.write(f"{web} | {mail} | {passw}")
                f.write("\n")

            website_entry.delete(0, END)
            pass_entry.delete(0,END)


def random_pass():
    pass_entry.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []

    a=random.randint(2,4)
    n=random.randint(2,4)
    s=random.randint(2,4)

    for char in range(1,int(a)+1):
        randomchar = random.choice(letters)
        password += randomchar

    for char in range(1,int(n)+1):
        randomchar = random.choice(numbers)
        password += randomchar

    for char in range(1,int(s)+1):
        randomchar = random.choice(symbols)
        password += randomchar


    random.shuffle(password)
    strong_pass = "".join(password)
    

    pass_entry.insert(0,f"{strong_pass}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(500,400)
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width = 200,height =200)
logo_image = PhotoImage(file="day 29, password gui/logo.png")
canvas.create_image(100,100,image = logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text = "Website:")
website_label.grid(column=0, row=1)
email_label = Label(text = "Email/Username:")
email_label.grid(row=2,column=0)
pass_label = Label(text = "Password:")
pass_label.grid(row=3, column=0)



website_entry = Entry(width =35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width =35)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0,"habeeb@gmail.com")

pass_entry = Entry(width = 21, show = "*")
pass_entry.place(x=120,y=263)


gen_button = Button(text = "Generate Password",width = 11, command = random_pass)
gen_button.grid(column=2, row= 3)


add_button = Button(text = "Add",command = save_file)
add_button.grid(row=4, column=1, columnspan=2)
add_button.config(width = 35)







window.mainloop()
