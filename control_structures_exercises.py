from calendar import weekday
import datetime

#1a. prompt the user for a day of the week, print out whether the day is Monday or not

today = str(input("Input day of the week: ").capitalize())

if today == "Monday":
    print("Today is Monday!")
else:
    print("Today is not monday.")

#1b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

today = str(input("input day of the week: ").capitalize())
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Satuday", "Sunday"]

if today in weekday:
    print("Today is a weekday.")
else:
    (print("Today is a weekend."))

#1c.
# create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

import babel.numbers     

hourly_pay_rate = 25
hours_worked_this_week = 45 #given these variables, output should be $1187.50
weekly_wage = 0

if hours_worked_this_week < 40:
    weekly_wage = hours_worked_this_week * hourly_pay
elif hours_worked_this_week > 40:
    weekly_wage = (hourly_pay_rate * 40 ) + ((hours_worked_this_week - 40) * (hourly_pay_rate * 1.5))

print(babel.numbers.format_currency(weekly_wage, "USD", locale = "en_US"))

#2a. Loop Basics
# While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line

i = 0

while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.

i = 100

while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

i = 2

while i < 1000000:
    print(i)
    i **= 2

# Write a loop that uses print to create the output shown below
# 100
# 95
# 90
# 85
# 80
# 75...5 (end)

i = 100

while i >= 5:
    print(i)
    i -= 5

#2b. For Loops
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# For example, if the user enters 7, your program should output:

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

number_table = int(input("enter number: "))

for i in range(1, 11): #this 'range' for loop will iterate from 1-11 (exlusive of 11, so 1-10)
    print(number_table, "x", i, "=", number_table*i) #this print statement will print the 'input' number, 'visual' string text to display the number table similar to example output and the input number (x) each number in the range for loop 1-10

# 2c. Create a for loop that uses print to create the output shown below.

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

x = 1

for i in range(x):
    


        
