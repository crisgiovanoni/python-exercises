import numpy as np
from statistics import mean
from math import prod
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = mean(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

prod = 1
for num in a:
    prod *= num

product_of_a = [prod]
print(product_of_a)
    
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = []

for num in a:
    num = num ** 2
    squares_of_a.append(num)

print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = []

for num in a:
    if num % 2 != 0:
        odds_in_a.append(num)

print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = []

for num in a:
    if num % 2 == 0:
        evens_in_a.append(num)

print(evens_in_a)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

type(b) # check the type of b; a list
b = np.array(b) # convert b from a list to a numpy array
type(b) # re-check if b is now a numpya array

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

print(sum_of_b)

b.sum()

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

# Cris Note: trying to understand the logic of min_of_b above
# b_clone = [
#     [3, 4, 5],
#     [6, 7, 8]
# ]
# min(b_clone[0])
# min(b_clone[1])
# max(b_clone[0])

b.min()
# Min in numpy doesn't work like the above logic. It aggregates everything together and finds the min. It could be thousands of arrays, and it will just loop through every element in the array compressed together as one array.

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

b.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))

b.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

b.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = b ** 2
print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[b % 2!= 0]
print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
print(evens_in_b)

# Exercise 9 - print out the shape of the array b.

b.shape

# Exercise 10 - transpose the array b.
np.transpose(b)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.reshape((1,6))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape((6,1))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

type(c)
c = np.array(c)
type(c)
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

c.min()
c.max()
c.sum()
c.prod()

# Exercise 2 - Determine the standard deviation of c.

c.std()

# Exercise 3 - Determine the variance of c.

c.var()

# Exercise 4 - Print out the shape of the array c

c.shape

# Exercise 5 - Transpose c and print out transposed result.

c_transposed = np.transpose(c)
print(c_transposed)

# Exercise 6 - Multiply c by the c-Transposed and print the result.

prod_c_and_ctrans = c * c_transposed
print(prod_c_and_ctrans)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

prod_c_and_ctrans.sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

prod_c_and_ctrans.prod()

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

type(d)
d = np.array(d)
type(d)

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)

# Exercise 4 - Find all the negative numbers in d
all_negatives = d[d < 0]
print(all_negatives)

# Exercise 5 - Find all the positive numbers in d
all_positives = d[d>0]
print(all_positives)

# Exercise 6 - Return an array of only the unique numbers in d.
only_unique = np.unique(d)
type(only_unique)
print(only_unique)

# Exercise 7 - Determine how many unique numbers there are in d.
len(only_unique)

# Exercise 8 - Print out the shape of d.
d.shape

# Exercise 9 - Transpose and then print out the shape of d.
d_transpose = np.transpose(d)
print(d_transpose)

# Exercise 10 - Reshape d into an array of 9 x 2
d_reshape = d.reshape((9,2))
print(d_reshape)