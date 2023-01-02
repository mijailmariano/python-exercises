# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list

numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.

numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string

output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
uppercased.fruits = [fruit.upper() for fruit in fruits]

print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
capitalized_fruits = [fruit.title() for fruit in fruits]

print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
vowels = ['a', 'e', 'i', 'o', 'u']
fruits_with_more_than_two_vowels = [fruit for fruit in fruits (vowel for vowel in vowels) if v]

print(fruits_with_more_than_two_vowels)

#notes
#i need to 'isolate' each fruit in the list called 'fruits'
#i then need to look at each letter in the fruit name -- consider using a 'split()' method
#and compare each 'fruit letter' with vowels/letters in the list called 'vowels'
#the fruit name must must meet the condition of 2 or more vowels to be appended to the new list


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

#notes
#i need to 'isolate' each fruit in the list called 'fruits'
#i then need to look at each letter in the fruit name -- consider using a 'split()' method
#and compare each 'fruit letter' with vowels/letters in the list called 'vowels'
#keep a running count of ea. fruit letter that is a vowel
#if fruit contains exactly two(2) vowels, append the fruit to list
#once i've iterated thru all 'fruits', return those fruit name that meet condition

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
vowels = ['a', 'e', 'i', 'o', 'u']
fruits_with_only_two_vowels = [fruit for fruit in fruits if sum(fruit.count(vowel) for vowel in vowels) == 2]

print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_more_than_five_characters = [fruit for fruit in fruits if(len(fruit) > 5)]

print(fruits_with_more_than_five_characters)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_five_characters = [fruit for fruit in fruits if len(fruit) == 5]

print(fruits_with_five_characters)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_less_than_five_characters = [fruit for fruit in fruits if len(fruit) < 5]

print(fruits_with_less_than_five_characters)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruit_characters = [len(fruit) for fruit in fruits]

print(fruit_characters)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_letter_a = [fruit for fruit in fruits if "a" in fruit]

print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

numbers = [0, 10, 20, 7, -2]
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

numbers = [0, 10, 20, 7, -2]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

numbers = [10, 7, -399, 15, 9, 20, 12, -1]
positive_numbers = [num for num in numbers if num >= 0]

print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

numbers = [10, 80, -20, -2, 9]
negative_numbers = [num for num in numbers if num < 0]

print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

lst_of_numbers = [2, 10, 299, 0, 8, 27, 4, 29999]
numbers_with_two_or_more_digits = [num for num in lst_of_numbers if abs(num) >= 10]

print(numbers_with_two_or_more_digits)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers = [2, 3, 4, 5, 6]
numbers_squared = [num**2 for num in numbers]

print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

numbers = [-1, -3, 4, -27, -7.97]
odd_negative_numbers = [num for num in numbers if abs(num) % 2 != 0 and num < 0] #for negative numerical values and in instances where you are not getting back the expected return values, consider using 'abs()' method instead of using modulo operator 

print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

numbers = [10, 0, 5, 30, 2]
numbers_plus_5 = [num+5 for num in numbers]

print(numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

import sympy
numbers = [2, 1, 4, 5, 7, 29, -99, 9.17]
primes = [num for num in numbers if sympy.isprime(num)]

print(primes)