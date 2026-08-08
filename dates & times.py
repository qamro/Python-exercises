import datetime

# set a specific date
date = datetime.date(2008, 2, 28) # year, month, day
print(f"My birthday is: {date}")
print()

# get today's date
today = datetime.date.today()
print(f"Today's date is: {today}")
print()

# set a specific time
time = datetime.time(15, 30, 25) # hour, minute, second
print(f"The time is: {time}")
print()

# get the current time and date
now = datetime.datetime.now()
print(f"The current date and time is: {now}")
# we specify the format of the date and time using strftime()
now = now.strftime("%Y-%m-%d %H:%M:%S") # year-month-day hour:minute:second
print(f"The current date and time is: {now}")
print()

# set a specific date and time
date_time = datetime.datetime(2008, 2, 28, 15, 30, 25) # year, month, day, hour, minute, second
print(f"The specific date and time is: {date_time}")