##################### Extra Hard Starting Project ######################
PLACEHOLDER = "[NAME]"
import datetime as dt
import pandas as pd
import random
import smtplib
import os

my_email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
today = now.day
month = now.month
for index, row in df.iterrows():
    if row["month"] == month and row["day"] == today:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letters = ["Letters/letter_1.txt", "Letters/letter_2.txt", "Letters/letter_3.txt"]
        chosen_letter = random.choice(letters)
        with open(chosen_letter, "r") as f:
            letter_content = f.read()
        new_letter = letter_content.replace(PLACEHOLDER, row["name"])
        with open("birthday_letter.txt", "w") as data_file:
            final_letter = data_file.write(new_letter)
        with open("birthday_letter.txt", "r") as f:
            email_content = f.read()

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row["email"],
                                msg=f"Subject:Happy Birthday!\n\n{email_content}")


