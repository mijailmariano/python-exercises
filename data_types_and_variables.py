


# Create a Python script file named data_types_and_variables.py. Inside it, write some Python code, that is, variables and operators, to describe the following scenarios. Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code.

# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?


little_mermaid = 3
brother_bear = 5
hercules = 1
per_day_rental_cost = 3

total_rental_costs = (little_mermaid + brother_bear + hercules) * per_day_rental_cost

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_pay_rate = 400
google_hrs_worked = 6

amazon_pay_rate = 380
amazon_hrs_worked = 4

facebook_pay_rate = 350
facebook_hrs_worked = 10

weekly_salary = (google_pay_rate * google_hrs_worked) + (amazon_pay_rate * amazon_hrs_worked) + (facebook_pay_rate * facebook_hrs_worked)


# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

#steps
#check if any days in the student's schedule are in the class schedule
#if no conflict -- then print true
#if >= 1 conflict -- then print false

student_enrolled = None
student_schedule = ["tuesday"] #for all inputs - i will need to find a way to capture both lower and upper inputs 
class_status = "not full"
class_schedule = ["monday", "tuesday", "thursday", "friday"]

if class_status != "full":
    if not student_schedule:
        student_enrolled = True
    else:
       if any(day in student_schedule for day in class_schedule):
           student_enrolled = False
           print(student_enrolled)
       else:
           student_enrolled = True
           print(student_enrolled)
else: print("Full class. Student cannot enroll.")

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

#steps
#create some variables 
#1a.customer type (normal vs. premium)
#1b. number of items purchased/in basket
#2. offer expired (yes/no?) can also be a date

import datetime
from operator import truediv
current_date = datetime.datetime.today()

customer_type = str(input("member status (normal/premium): ")) #could also add someway of validating this
products = int(input("number of products in basket: "))
offer_expiration = datetime.datetime(2022, 5, 30)

if customer_type == "premium member" and current_date <= offer_expiration:
    print("offer can be applied!")
elif customer_type != "premium member" and current_date <= offer_expiration and products >= 2:
    print("offer can be applied!")
else:
    print("offer cannot be applied.")


# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace


while True:
    username = input('enter username: ')
    password = input('enter password: ')
    if len(password) >= 5 and len(password) <= 20 and password != username:
        if username != username.strip() and password != password.strip(): # here i am saying if username and password do not equal strip method (containing whitespace in either front or back of string), then access granted 
            print("Acceess Granted!")
            break
        else: 
            print('Invalid password. Try again.')


