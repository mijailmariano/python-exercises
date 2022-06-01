from ast import While
from calendar import weekday
from curses.ascii import isdigit
import datetime
from multiprocessing.sharedctypes import Value

#1a. prompt the user for a day of the week, print out whether the day is Monday or not

today = input("Input day of the week: ").capitalize()

if today == "Monday":
	print("Today is Monday!")
else:
	print("Today is not Monday.")

#1b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

today = input("input day of the week: ").capitalize()

#first, make sure input is valid:
#e.g., while today/input() not in full list of days in the week
#print('some text telling user to re-input a value')
#re-enter an appropriate input

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Satuday", "Sunday"]
days_in_the_week = ["Satuday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

while today not in days_in_the_week:
	print("invalid input. try again")
	today = input("input day of the week: ").capitalize()

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

for num in range(1, 11): #this 'range' for loop will iterate from 1-11 (exlusive of 11, so 1-10)
	print(number_table, "x", num, "=", number_table*num) #this print statement will print the 'input' number, 'visual' string text to display the number table similar to example output and the input number (x) each number in the range for loop 1-10

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

for num in range(10): #the range here will be from 0-9
	print(str(num) * num) #the "first print" will not print because the iteration begins at "0" (e.g., str(0) * 0)
	#every other iteration will print beginning at "str(1)" thru "str(9)"

#2d. break and continue
# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
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

else:
	for num in range(1, 50):
		if num == int(user_input):
			print("Yikes! Skipping number: ", num)
			continue 
		print("Here is an odd number: ", num)


# other approach
# while True:
# 	if num.isdigit() == False or int(num) > 50 or int(num) < 1 or int(num) % 2 == 0:
# 		print("invalid number. try again")
# 		num = input("enter number between 1 - 50: ") 
# 	else: 
# 		break

# ...now you can go into the needed iteration prompt


# 2e.The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

user_number = input("Enter a positive number: ")

while int(user_number) < 0:
	print("Invalid entry. Try again.")
	user_number = input("Enter a positive number: ")
else: 
	for num in range(int(user_number)+1):
		print(num)


# 2f. Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

pos_integer = input("enter positive integer: ")

while int(pos_integer) < 0:
	print("Invalid entry. Try again.")
	pos_integer = input("enter positive integer: ")
else:
	for num in range(int(pos_integer), 0, -1): #here i am using the range() "start, stop, and step" so i am essentially saying, start counting at pos_int number(which is inclusive), stop at '0'(which is exclusive, so will stop at 1), and step or substract from starting position by 1
		print(num)


# 3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100

for num in range(1, 101):
	print(num)

# For multiples of three print "Fizz" instead of the number

for num in range(1, 101):
	if num % 3 == 0:
		print("Fizz", "|", num)

# For the multiples of five print "Buzz"

for num in range(1, 101):
	if num % 5 == 0:
		print("Buzz", "|", num)

# For numbers which are multiples of both three and five print "FizzBuzz"

for num in range(1, 101):
	if num%2 == 0 and num%5 == 0:
		print("FizzBuzz", "|", num)

#combining it all
for num in range(1, 101):
	if num%2 == 0 and num%5 == 0:
		print("FizzBuzz", "|", num)
	elif num % 3 == 0:
		print("Fizz", "|", num)
	elif num % 5 == 0:
		print("Buzz", "|", num)
	else:
		print(num)

# 4. Display a table of powers.

# Prompt the user to enter an integer.
integer_num = input("enter an integer: ")

# Display a table of squares and cubes from 1 to the value entered.

for num in range(1, int(integer_num)+1):
	print(num, num**2, num**3)

# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output
# -----
# integer_num = input("enter an integer: ")
# count = int(integer_num)

# while count > 0 or count < 0:
# 	for num in range(1, int(integer_num)+1):
# 		print(num, num**2, num**3)
# 		count -= 1
# 		if count == 0:
# 			cont_yes_or_no = input("Do you wish to continue? (yes or no): ").upper()
# 			if cont_yes_or_no == "YES":
# 				enter_another_interger = input("enter another integer: ")
# 					for num in range(1, int(enter_another_interger)+1):
# 						print(num, num**2, num**3)
# else: exit()

# 5. Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100
# Display the corresponding letter grade
# Prompt the user to continue
# Assume that the user will enter valid integers for the grades
# The application should only continue if the user agrees to
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

numerical_grade = int(input("Enter your grade as 0 - 100: "))
grade_ranges = ["A: 100 - 88", "B: 87 - 80", "C: 79 - 67", "D: 66 - 60", "F: 59 - 0"]

if numerical_grade <= 100 and numerical_grade >= 88:
	letter_grade = "A"
	print("Your letter grade is: ", letter_grade)
	cont_response = input("Do you wish to continue? (enter yes or no): ")
	if cont_response.upper() == "YES":
		for i in grade_ranges:
			print(i)
	else: print("All done!")
elif numerical_grade <= 87 and numerical_grade >= 80:
	letter_grade = "B"
	print("Your letter grade is: ", letter_grade)
	cont_response = input("Do you wish to continue? (enter yes or no): ")
	if cont_response.upper() == "YES":
		for i in grade_ranges:
			print(i)
	else: print("All done!")
elif numerical_grade <= 79 and numerical_grade >= 67:
	letter_grade = "C"
	print("Your letter grade is: ", letter_grade)
	cont_response = input("Do you wish to continue? (enter yes or no): ")
	if cont_response.upper() == "YES":
		for i in grade_ranges:
			print(i)
	else: print("All done!")
elif numerical_grade <= 66 and numerical_grade >= 60:
	letter_grade = "D"
	print("Your letter grade is: ", letter_grade)
	cont_response = input("Do you wish to continue? (enter yes or no): ")
	if cont_response.upper() == "YES":
		for i in grade_ranges:
			print(i)
	else: print("All done!")
elif numerical_grade <= 59 and numerical_grade >= 0:
	letter_grade = "F"
	print("Your letter grade is: ", letter_grade)
	cont_response = input("Do you wish to continue? (enter yes or no): ")
	if cont_response.upper() == "YES":
		for i in grade_ranges:
			print(i)
	else: print("All done!")
 
 #other class approach

# while True:
# 	num = input("please enter the numeric grade: ")
# 	num = int(num)
# 	if num >= 88:
# 		print('A')
# 	elif num etc...


# 6. Create a list of dictionaries where each dictionary represents a book that you have read. 
# a. Each dictionary in the list should have the keys title, author, and genre. 
# b. Loop through the list and print out information about each book.
# c. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

lst_of_dictionaries = [{"title": "Man's Search for Meaning", "author": "Victor Frankl", "genre": "psychology"}, {"title": "Learn to Code By Solving Problems", "author": "Daniel Zingaro", "genre": "programming"}, {"title": "Nudge", "author": "Daniel Zingaro", "genre": "psychology"}]
print(lst_of_dictionaries[0]["title"]) #here iam looking at the "0/first indexed" dictionary, and printing the value of the key named "title"
print(lst_of_dictionaries[1]['aurthor']) #here iam looking at the "1/second indexed" dictionary and printing the value of the key named "aurthor"

#other class approach

for book in lst_of_dictionaries:
	print(f"The book {book['title']} by {book['author']} belongs to genre {book['genre']}")

#notes
#create an input variable that prompts a user to enter a book genre
#iterate thru the lst_of_dictionaries
#look at each dictionary's key named "genre"
#if the key's genre matches the user's input genre
#return/print all values for the key "title" for that dictionary

user_genre = input("Enter interested book genre: ")
lst_of_dictionaries = [{"title": "Man's Search for Meaning", "author": "Victor Frankl", "genre": "psychology"}, {"title": "Learn to Code By Solving Problems", "aurthor": "Daniel Zingaro", "genre": "programming"}, {"title": "Nudge", "aurthor": "Richard Thaler and Cass Sunstein", "genre": "psychology"}]
for dictionary in lst_of_dictionaries:
	if dictionary["genre"] == user_genre:
		print(dictionary['title'])



#trying a different approach here
# user_genre = input("Enter interested book genre: ")
# lst_of_dictionaries = [{"title": "Man's Search for Meaning", "author": "Victor Frankl", "genre": "psychology"}, {"title": "Learn to Code By Solving Problems", "aurthor": "Daniel Zingaro", "genre": "programming"}, {"title": "Nudge", "aurthor": "Richard Thaler and Cass Sunstein", "genre": "psychology"}]
# lst_of_matching_titles = ()
# for dictionary in lst_of_dictionaries:
# 	if dictionary["genre"] == user_genre:
# 		lst_of_matching_titles.append(dictionary['title'])
# 	else: continue

# print(lst_of_matching_titles)
	

	






