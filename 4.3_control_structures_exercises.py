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
print("Pick any day of the week: ")
day_of_week = input(" ")

if day_of_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
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

print("Give a base no. to multiply: ")
number = input(" ")

for number in range(1,11):
    print(input() + "x" + str(number) + "=" + (str(input() * number))

# Create a for loop that uses print to create the output shown below.

j = 1

for number in range(1,10):
    prod = number * j
    print(prod)
    number += 1
    j *= 10