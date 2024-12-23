import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
week = now.weekday()

file = open("day 32 smtp/quotes.txt")

if week == 1:
    read =file.readlines()
    random_quote = random.choice(read)
    my_email = "habeebsait04@gmail.com"
    password = "***"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    message = f"Subject: Quote of the day\n\nr{random_quote}"
    connection.sendmail(from_addr=my_email, to_addrs="habeebsait24@gmail.com", msg=message)
    connection.close()
    file.close()
