import smtplib
#
my_email = "primefire0.3@gmail.com"
password = "zsstiwtphbpoojli"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="tonysmith0730@outlook.com",
#                         msg="Subject:Hi!\n\nThis is my response to your previous email.") #This way you can add a subject and content of the email.

import datetime as dt
from random import choice

now = dt.datetime.now()
today = now.weekday()
friday = 4
# if today == friday:
with open("quotes.txt", "r") as f:
    quotes = f.readlines()

if today == friday:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="tonysmith0730@outlook.com", msg=f"Subject:Motivational Quote\n\n{choice(quotes)}")




# date_of_birth = dt.datetime(year=2004, month=7, day=30)
# print(date_of_birth)