from ast import While
from calendar import weekday
from curses.ascii import isdigit
import datetime
from unicodedata import digit

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

for i in range(10): #the range here will be from 0-9
    print(str(i) * i) #the "first print" will not print because the iteration begins at "0" (e.g., str(0) * 0)
    #every other iteration will print beginning at "str(1)" thru "str(9)"

#3a. break and continue
# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# Your output should look like this:

#notes
#prompt user to type a number
#number must be an odd number > 1 and < 50
#start by evaluating the "enetered" string by using ".isdigit()" method
#if string is not a numeric value, or > 1, or < 50 then prompt user to "re-enter a valid value"
#else -- 
#turn user_input into "integer"
#run a "for loop" ranging 1-50
#once for loop reaches the entered user_input; print..."yikes statement" and continue until 49

user_input = input("enter an odd number from 1 - 50: ")

while int(user_input) < 1 or int(user_input) > 50 or int(user_input) % 2 == 0:
    print("Invalid input. Try again.")
    user_input = input("enter an odd number from 1 - 50: ")
    break

for i in range(1, 50):
    if i == int(user_input):
        print("Yikes! Skipping number: ", i)
        continue 
    print("Here is an odd number: ", i)

# 3b.The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

input_positive_number = int(input("Enter a positive number: "))

while type(input_positive_number) = int:


else:
    print("Invalid input. Enter positive value.")
    input_positive_number = int(input("Enter a positive number: "))




# 3c. Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.