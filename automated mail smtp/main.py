import pandas as pd
import random
import smtplib
import datetime as dt


my_email = "****your mail****"
password = "***password****"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day


file = pd.read_csv("birthdays.csv")
file_dict = file.to_dict(orient = "records")


for i in range(len(file_dict)):
    if month == file_dict[i]["month"] and day == file_dict[i]["day"]:

        letter_path = random.choice(["letter_1.txt","letter_2.txt", "letter_3.txt"])
        letter = open(letter_path)
        letter_content = letter.read()
        new_letter = letter_content.replace("[NAME]", file_dict[i]["name"])

        connection = smtplib.SMTP("smtp.gmail.com", 587)  # if this doesnt work search mail smtp address (your mail)
        connection.starttls()
        connection.login(user = my_email, password=password)
        message = new_letter
        connection.sendmail(from_addr=my_email, to_addrs= file_dict[i]["email"], msg = f"Subject:Birthday Wish\n\n{message}")
        connection.close()
        letter.close()
    



