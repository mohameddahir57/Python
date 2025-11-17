# Day 25 :Automation with Python (scripts, scheduling)
# Welcome to Day 27 of your Python learning journey! Today, we will explore how to automate tasks using Python scripts and scheduling. We will cover the basics of writing automation scripts and scheduling them to run at specific times using the `schedule` module.
# Automation can help you save time and reduce manual effort by automating repetitive tasks such as file management, data processing, and more.
# Table of Contents
# 1. [Writing Automation Scripts](#writing-automation-scripts)
# 2. [Scheduling Automation](#scheduling-automation)
# 3. [Practice Exercises](#practice-exercises)

# Writing Automation Scripts
# To write automation scripts, you can use Python as a scripting language. Here's an example of a simple script that creates a new file:
import os
def create_file(file_path):
    with open(file_path, 'w') as file:
        file.write("Hello, world!")
# Usage
file_path = 'new_file.txt'
create_file(file_path)
print(f"File '{file_path}' created successfully.")

# Scheduling Automation
# You can schedule your automation scripts to run at specific times using the `schedule` module. First, you need to install the `schedule` module if you haven't already:
# pip install schedule
# Here's an example of scheduling a script to run every hour:
import schedule
import time
def my_script():
    print("Running my automation script...")
    # Add your automation code here
schedule.every(1).hours.do(my_script)
while True:
    schedule.run_pending()
    time.sleep(1)

# Practice Exercises
# 1. Write a script that deletes all files in a specified directory that are older than 7 days.
import os
import datetime
def delete_old_files(directory, days):
    now = datetime.datetime.now()
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and (now - datetime.datetime.fromtimestamp(os.path.getmtime(file_path))).days > days:
            os.remove(file_path)
# Usage
delete_old_files('/path/to/directory', 7)   
# 2. Write a script that sends an email to a specified recipient every day at a specific time.
import smtplib
import datetime
def send_email(recipient, subject, message):
    now = datetime.datetime.now()
    if now.hour == 12 and now.minute == 0:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email', 'your_password')
        server.sendmail('your_email', recipient, f"Subject: {subject}\n\n{message}")
        server.quit()
# Usage
send_email('TQ6tq@example.com', 'Daily Reminder', 'Hello, this is a daily reminder.')   

# Note: Make sure to replace 'your_email' and 'your_password' with your actual email credentials. Also, be cautious when using email automation to avoid spamming.
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                    (id INTEGER PRIMARY KEY, name TEXT, price REAL)''') 
connection.commit()
connection.close()

# 3. Write a script that backs up a specified directory to another location every week.
import shutil
import datetime
def backup_directory(source, destination):
    now = datetime.datetime.now()
    if now.weekday() == 0:  # Monday
        shutil.copytree(source, destination, dirs_exist_ok=True)
# Usage
backup_directory('/path/to/source', '/path/to/destination')
# Congratulations on completing Day 27! You've learned how to write automation scripts and schedule them using Python. Keep practicing and exploring more automation possibilities with Python!
# Note: Make sure to replace '/path/to/directory', '/path/to/source', and '/path/to/destination' with actual paths on your system.