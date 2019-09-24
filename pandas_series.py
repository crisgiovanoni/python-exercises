# Use pandas to create a Series from the following data:

import pandas as pd
import matplotlib.pyplot as plt

# Name the variable that holds the series fruits.
fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruits = pd.Series(fruits)

# Run .describe() on the series to see what describe returns for a series of strings.
fruits.describe()

# Run the code necessary to produce only the unique fruit names.
fruits.unique()

# Determine how many times each value occurs in the series.
fruits.value_counts()

# Determine the most frequently occurring fruit name from the series.
fruits.mode()

# Determine the least frequently occurring fruit name from the series.
fruits.nsmallest()

least_frequent = fruits.value_counts().min()
least_frequent

frequencies = fruits.value_counts()
frequencies

frequencies[frequencies == least_frequent]

# Write the code to get the longest string from the fruits series.
fruits.str.len().idxmax()

fruit_names = fruits.unique()
fruit_names = pd.Series(fruit_names)
length_of_longest_string = fruit_names.str.len().max() # the length of the longest string
index_of_longest_string = fruit_names.str.len().idxmax() # the index of the longest string
longest_string = fruit_names[index_of_longest_string]

print("The longest string in the list of fruits is", longest_string, "and it has", length_of_longest_string)

# handling multiple longest_string
length_of_longest_string = fruit_names.str.len().max() #length of longest string
length_of_longest_string
fruit_names[fruit_names.str.len() == length_of_longest_string]

# Find the fruit(s) with 5 or more letters in the name.

five_or_more = fruits.apply(lambda x:len(x) >= 5)
fruits[five_or_more] #boolean masking/indexing

# Capitalize all the fruit strings in the series.
fruits.str.capitalize()

# Count the letter "a" in all the fruits (use string vectorization)

counts_of_a = fruit_names.str.count("a")
counts_of_a
fruit_names
counts_of_a

list(zip(fruit_names, counts_of_a))

#another approach
for i, fruit in enumerate(fruit_names):
    print(fruit,"has",counts_of_a[i],"number of 'a' characters.")

# Output the number of vowels in each and every fruit.

def count_vowels(word):
    count = 0
    for n in word:
        if n.lower() in "aeiou":
            count += 1
    return count

fruits.apply(count_vowels)

# series.apply(lambda n: 'even' if n % 2 == 0 else 'odd')

# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.
fruits.get_values.apply(lambda x: x.count("o") >= 2)

# count_g = lambda x: x.count("g")
# Write the code to get only the fruits containing "berry" in the name
fruits.(lambda x: x in "berry")

# Write the code to get only the fruits containing "apple" in the name
fruits.apply(lambda x: x in "berry")

# Which fruit has the highest amount of vowels?
fruits.apply(count_vowels).sum()

# Use pandas to create a Series from the following data:

assets = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

assets = pd.Series(assets)

# What is the data type of the series?
assets.dtype

# Use series operations to convert the series to a numeric data type.
assets = assets.str.replace(",","")
assets = assets.str.replace("$","")
assets = assets.astype(float)

# What is the maximum value? The minimum?
assets.max()
assets.min()

# Bin the data into 4 equally sized intervals and show how many values fall into each bin.
assets_binned = pd.cut(assets, 4)
print(assets_binned)
print(assets)

# Plot a histogram of the data. Be sure to include a title and axis labels.
pd.Series(assets).plot.hist(edgecolor = "gray", color = "mistyrose")
plt.title("Assets")
plt.xlabel("Amount in $")
plt.ylabel("Observations")

# Use pandas to create a Series from the following exam scores:
scores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
scores = pd.Series(scores)

# What is the minimum exam score? The max, mean, median?
scores.min()
scores.max()
scores.mean()
scores.median()

# Plot a histogram of the scores.
pd.Series(scores).plot.hist(edgecolor = "gray", color = "lightcoral")

# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.

def convert_grade(n):
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    elif n >= 61:
        return "D" 
    elif n <= 60:
        return "F"

scores.apply(convert_grade)

# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.

scores
scores_curved = scores + (100 - scores.max())
scores_curved

# Use pandas to create a Series from the following string:

super_cali = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
super_cali
super_cali = pd.Series(super_cali)

# What is the most frequently occuring letter? Least frequently occuring?
super_cali.mode()

super_cali.value_counts().idxmin()
# How many vowels are in the list?
# How many consonants are in the list?
# Create a series that has all of the same letters, but uppercased
# Create a bar plot of the frequencies of the 6 most frequently occuring letters.