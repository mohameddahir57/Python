#Day 19-Dates & Times (datetime module, formatting, timedelta)
#Welcome to Day 16 of your Python learning journey! Today, we will explore dates and times in Python using the datetime module. We will learn how to work with datetime objects, format dates and times, and calculate time differences.
## Table of Contents  
#1. [Working with Dates and Times](#working-with-dates-and-times)
#2. [Formatting Dates and Times](#formatting-dates-and-times)
#3. [Calculating Time Differences](#calculating-time-differences)
#4. [Practice Exercises](#practice-exercises)   

#1. Import the datetime module and get the current date and time.
import datetime
now = datetime.datetime.now()
print(now)

#2. Format a date as a string in a specific way.
date_str = now.strftime("%Y-%m-%d")
print(date_str)

#3. Calculate the difference between two dates.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
time_diff = end_date - start_date
print(time_diff)

#4. Convert a string to a datetime object.
date_str = "2023-06-15"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print(date_obj)

#5. Calculate the number of days between two dates.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
days_diff = (end_date - start_date).days
print(days_diff)

#6. Calculate the number of hours between two dates.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
hours_diff = (end_date - start_date).total_seconds() / 3600
print(hours_diff)

#7. Calculate the number of minutes between two dates.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
minutes_diff = (end_date - start_date).total_seconds() / 60
print(minutes_diff)

#8. Calculate the number of seconds between two dates.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
seconds_diff = (end_date - start_date).total_seconds()
print(seconds_diff)

#9. Calculate the number of weeks between two dates.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
weeks_diff = (end_date - start_date).days // 7
print(weeks_diff)

#10. Calculate the number of months between two dates.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
months_diff = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
print(months_diff)

#11. Calculate the number of years between two dates.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
years_diff = end_date.year - start_date.year
print(years_diff)

#12. Calculate the number of days between two dates, including leap years.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2024, 2, 29)
days_diff = (end_date - start_date).days
print(days_diff)

#13. Calculate the number of hours between two dates, including leap years.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2024, 2, 29, 12, 0)
hours_diff = (end_date - start_date).total_seconds() / 3600
print(hours_diff)

#14. Calculate the number of minutes between two dates, including leap years.
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2024, 2, 29, 12, 0)
minutes_diff = (end_date - start_date).total_seconds() / 60
print(minutes_diff)


