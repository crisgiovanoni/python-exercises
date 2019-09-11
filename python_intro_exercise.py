99.9 == float
"False" == string
False == boolean
'0' == string
0 == integer
True == boolean
'True' == string
[{}] == list
{'a': []} == dictionary

# What data type would best represent:
A term or phrase typed into a search box? == string
If a user is logged in? =
A discount amount to apply to a user/'s shopping cart? == float
Whether or not a coupon code is valid? == boolean
An email address typed into a registration form? == string
The price of a product? == float
A Matrix? == 
The email addresses collected from a registration form? == string
Information about applicants to Codeup's data science program? == string

# For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.

'1' + 2 #error
6 % 4 #2
type(6 % 4) #int
type(type(6 % 4)) #string; correct answer: type
'3 + 4 is ' + 3 + 4 # error
0 < 0 #False
'False' == False #False
True == 'True' #False
5 >= -5 #True
!False or False #True, correct answer: not returned
True or "42" #True
!True && !False #False' correct answer: error
6 % 5 #1
5 < 4 and 1 == 1 #False
'codeup' == 'codeup' and 'codeup' == 'Codeup' #False
4 >= 0 and 1 !== '1' #error
6 % 3 == 0 #True
5 % 2 != 0 #True
[1] + 2 #error
[1] + [2] #[1, 2]
[1] * 2 #[1], [1]; correct answer [1, 1]
[1] * [2] #2; correct answer: error
[] + [] == [] #True
{} + {} #{}; correct answer: error

# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
daily_price = 3
little_mermaid = daily_price * 3
brother_bear = daily_price * 5
hercules = daily_price * 1
rent = little_mermaid + brother_bear + hercules
print(rent)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google_rate = 400
amazon_rate = 380
facebook_rate = 350
week_payment = (10*facebook_rate) + (6*google_rate) + (4*amazon_rate)
print(week_payment)

# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_open = True
schedule_open = True
enrolled = class_open and schedule_open
print(enrolled)

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
cart = 0
premium_member = True
cart > 2 == True
offer_valid = True
apply_offer = premium_member + cart_count + offer_valid
print(apply_offer)

# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace
 
username = 'codeup'
password = 'notastrongpassword'

u_length = len(username) < 20
p_length = len(password) >= 5
up_distinct = username != password

if u_length == True and up_distinct == True,
    print("Username is valid")

if p_length == True and up_distinct == True,
    print("Password is valid")


# LIST COMPREHENSION #

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
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
vowels = {'a','e','i','o','u','A','E','I','O','U'}
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if fruit in vowels == 2]
print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_5_letters = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_with_more_than_5_letters)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_5_letters = [fruit for fruit in fruits if len(fruit) == 5]
print(fruits_with_5_letters)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_5_letters = [fruit for fruit in fruits if len(fruit) < 5]
print(fruits_with_less_than_5_letters)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
fruits_character_length = [len(fruit) for fruit in fruits]
print(fruits_character_length)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_a = [fruit for fruit in fruits if "a" in fruit]
print(fruits_with_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_numerals = [number for number in numbers if len(str(number)) >= 2]
print(two_numerals)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number ** 2 for number in numbers]
print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number % 2 != 0 and number < 0]
print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [number + 5 for number in numbers]
print(numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
import sympy

primes = [number for number in numbers if sympy.isprime(number) == True]
print(primes)