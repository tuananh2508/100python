# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
sum_days = int(365*90)
sum_weeks = int(52*90)
sum_months = int(12*90)

udays = int(age)*365
uweeks = int(age)*52
umonths = int(age)*12

days_left = sum_days - udays
months_left = sum_months - umonths
weekdays_left = sum_weeks - uweeks

print(f"You have {days_left} days, {weekdays_left} weeks, and {months_left} months left." )



