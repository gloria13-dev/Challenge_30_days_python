#Challenge python Day 16
#Exercises: Days 16
from datetime import datetime
from  datetime import timedelta

# 1 : the current day, month, year, hour, minute and timestamp
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(f'{day=}, {month=}, {year=}, {hour=}, {minute=}, {timestamp=}')

# 2:
now = datetime.now()
date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f'\nthe current date using the "%m/%d/%Y, %H:%M:%S" format is: {date}')

#3
date_str = "5 December, 2019"
converted_date = datetime.strptime(date_str, "%d %B, %Y")
print("\nConverted date:", converted_date)

#4: Time difference until New Year
new_year = datetime(2026, 1, 1)
time_left = new_year - now
print("\nTime left until New Year:", time_left)

#5
past = datetime(1970, 1, 1)
diff = now - past
print("\nTime difference between Jan 1, 1970 and now is: ", past)






