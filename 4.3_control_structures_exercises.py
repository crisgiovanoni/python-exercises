# Conditional Basics

# create variables and make up values for
# -the number of hours worked in one week
# -the hourly rate
# -how much the week's paycheck will be
# -write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# prompt the user for a day of the week, print out whether the day is Monday or not
print("Pick any day of the week: ")
day_of_week = input(" ")

if day_of_week == "Monday":
    print("Monday")
else:
    print("Not Monday")

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_of_week = input("Pick any day of the week: ")

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("Weekday")
else:
    print("Weekend")

# create variables and make up values for
# -the number of hours worked in one week
# -the hourly rate
# -how much the week's paycheck will be
# -write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
no_work_hours = 40
hourly_rate = 45
overtime_hour = 0
overtime_rate = overtime_hour + (overtime_hour/2)

pay_per_week = no_work_hours * hourly_rate + overtime_rate
print(pay_per_week)

# While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# Alter your loop to count backwards by 5's from 100 to -10.
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

i = 0

while i < 101:
    print(i)
    i += 2

i = 100

while i > -11:
    print(i)
    i -= 5

i = 2

while i < 1_000_000:
    print(i)
    i *= i

i = 100

while i > 4:
    print(i)
    i -=5

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

number = input("Pick a number: ")

for i in range(1,11):
    print(number + " x " + str(i) + " = " + str((int(number) * i)))
    i += 1

# Create a for loop that uses print to create the output shown below.

for number in range(1,2):
    for mult in (1,11,111,1111,11111,111111,1111111,11111111,111111111):
        recur = number * mult
        print(recur)
        number += 1

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
num = input("Pick an ODD number between 1 and 50: ")

#gatekeeper
while int(num) % 2 == 0:
    num = input("Pick an ODD number between 1 and 50: ")
    if int(num) >= 1 and int(num) <= 50 and int(num) % 2 != 0:
        break

num = int(num)

#loop
for i in range(1,50):
    if num == i:
        print("Yikes! Skipping number: " + str(i))
    elif num != i:
        print("Here is an odd number: " + str(i))

######## David's Solution
odd_num=""
while True:
    odd_num = input("Enter..")
    if odd_num.isdigit() and int(odd_num) % 2 ==1 and int(odd_num) > 1 and int(odd_num)<50:
        break
for i in range (1,50,2):
    if i ==int(odd_num):
        print("Yikes" + str(i))
        continue
    else:
        print("Here is an odd" + str(i))

# Prompt the user for an odd number between 1 and 50.
# Use a loop and a break statement to continue prompting the user if they enter invalid input.
# (Hint: use the isdigit method on strings to determine this).
# Use a loop and the continue statement to output all the odd numbers
# between 1 and 50, except for the number the user entered.

num = input("Pick an ODD number between 1 and 50: ")

while int(num) < 1 or int(num) > 50:
    num = input("Pick an ODD number between 1 and 50: ")
    if int(num) >= 1 and int(num) <= 50:
        break
for i in range(1,51):
    if i == num:
        continue
    print(i)

# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
number = input("Enter a POSITIVE number: ")

while int(number) <= 0:
    number = input("Enter a POSITIVE number: ")
    
number = int(number)

for i in range(0,number+1):
    print(i)

# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

number = input("Enter a POSITIVE number: ")

while int(number) <= 0:
    number = input("Enter a POSITIVE number: ")
    
number = int(number)

for i in range(number, 0,-1):
    print(i)

# Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.

for num in range(1,101):
    print(num)

# For multiples of three print "Fizz" instead of the number

for num in range(1,101):
    if num % 3 == 0:
        print("Fizz")
    else:
        print(num)

# For the multiples of five print "Buzz".

for num in range(1,101):
    if num % 5 == 0:
        print("Buzz")
    else:
        print(num)
# For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)

# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

# Example Output

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125

number = input("What number would you like to go up to? ")

number = int(number)

for i in range(1,number+1):
    print(i, i**2, i**3)

# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# Bonus

# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

grade = input("Enter a numerical grade from 0-100: ")

grade = int(grade)

if grade >= 88 and grade <= 100:
    print("A : 100 - 88")
elif grade >= 80 and grade <= 87:
    print("B : 87 - 80")
elif grade >= 67 and grade <= 79:
    print("C : 79 - 67")
elif grade >= 60 and grade <= 66:
    print("D : 66 - 60")
elif grade >= 0 and grade <= 59:
    print("F : 59 - 0")
else:
    print("Grade entered is invalid.")

Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

library = [
    {
        "title" : "The Seven Storey Mountain",
        "author" : "Thomas Merton",
        "genre" : "Autobiography"
    },
    {
        "title" : "Chronicles of Narnia",
        "author" : "C.S. Lewis",
        "genre" : "Fantasy"
    },
    {
        "title" : "The World's First Love",
        "author" : "Fulton Sheen",
        "genre" : "Non-fiction"
    }
    
]

for book in library:
    print(book)
    
genre_user = input("Choose a genre: ")

for book in library:
    if genre_user == book["genre"]:
        print(book)