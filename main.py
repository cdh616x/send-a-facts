import smtplib
import scraper
import datetime as dt
import keys

print(scraper.random_quote)

email = keys.email
password = keys.password

user_input = str(input("Would you like to send an email?"))

if user_input == "yes":
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=keys.rec_list,
                            msg=(f"Subject: Quotatia Automata\n\n{scraper.random_quote}"))

time_right_now = dt.datetime.now()
year = time_right_now.year
month = time_right_now.month
day = time_right_now.day
hour = time_right_now.hour
minute = time_right_now.minute
if minute < 10:
    minute = "0" + str(minute)
print(f"{month} {day}, {year} @ {hour}:{minute}")
