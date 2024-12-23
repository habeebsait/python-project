import pandas as pd
import random
import smtplib
import datetime as dt


my_email = "habeebsait04@gmail.com"
password = "ldgeekzegduqbzqn"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day


file = pd.read_csv("day 32 smtp/birthday-wisher-extrahard-start/birthdays.csv")
file_dict = file.to_dict(orient = "records")

print(len(file_dict))

# for i in range(2):
#     if month == file_dict[i]["month"] and day == file_dict[i]["day"]:

#         letter_path = random.choice(["day 32 smtp/birthday-wisher-extrahard-start/letter_templates/letter_1.txt","day 32 smtp/birthday-wisher-extrahard-start/letter_templates/letter_2.txt", "day 32 smtp/birthday-wisher-extrahard-start/letter_templates/letter_3.txt"])
#         letter = open(letter_path)
#         letter_content = letter.read()
#         new_letter = letter_content.replace("[NAME]", file_dict[i]["name"])

#         connection = smtplib.SMTP("smtp.gmail.com", 587)
#         connection.starttls()
#         connection.login(user = my_email, password=password)
#         message = new_letter
#         connection.sendmail(from_addr=my_email, to_addrs= file_dict[i]["email"], msg = f"Subject:Birthday Wish\n\n{message}")
#         connection.close()
#         letter.close()
    



