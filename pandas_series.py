# Use pandas to create a Series from the following data:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

fruit_names

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

fruits[fruits.apply(lambda x: x.count("o") >= 2)]

# Write the code to get only the fruits containing "berry" in the name
fruits[fruits.apply(lambda x: "berry" in x)]

# Write the code to get only the fruits containing "apple" in the name
fruits[fruits.apply(lambda x: "apple" in x)]

# Which fruit has the highest amount of vowels?
fruits[fruits.apply(count_vowels).idxmax()]

# Use pandas to create a Series from the following data:

assets = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

assets = pd.Series(assets)

# What is the data type of the series?
assets.dtype

# Use series operations to convert the series to a numeric data type.
assets = assets.str.replace(",","")
assets = assets.str.replace("$","")
assets = assets.astype(float)

str.lstrip

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

#other approach using bins
exam_scores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

letter_scores = pd.cut(exam_scores, bins = [0,60,70,80,90,100], labels = ['f','d','c','b','a'])

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

#misty's solution
super_cali[super_cali.value_counts() == super_cali.value_counts().mode()]

# How many vowels are in the list?

super_cali.apply(count_vowels).sum()

# How many consonants are in the list?

vowels = super_cali.apply(count_vowels).sum()

consonants = super_cali.count() - vowels
consonants

# Create a series that has all of the same letters, but uppercased
super_cali_ucase = super_cali.str.upper()
super_cali_ucase

# Create a bar plot of the frequencies of the 6 most frequently occuring letters.

frequencies = super_cali.value_counts()
frequencies

top_six_letters = frequencies.head(6)

top_six_letters.plot.bar(color = "lightslategray")

### DATA FRAME ###

from pydataset import data

mpg = data('mpg')

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)

# Create a column named passing_english that indicates whether each student has a passing grade in reading.

df["passing_english"] = df.reading >= 70
df

# Sort the english grades by the passing_english column. How are duplicates handled?
df
df.sort_values(by="passing_english")

# Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df
df.english.sort_values(["passing_english","name"])

# Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(["english","passing_english","name"])

# Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.
df["overall_grade"] = (df.math + df.english + df.reading)/3
df

# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

mpg

# How many rows and columns are there?

mpg.shape
#234 rows, 11 columns

# What are the data types of each column?
mpg.dtypes
# manufacturer     object
# model            object
# displ           float64
# year              int64
# cyl               int64
# trans            object
# drv              object
# cty               int64
# hwy               int64
# fl               object
# class            object
# dtype: object

# Summarize the dataframe with .info and .describe
mpg.describe()
mpg.info

# Rename the cty column to city.
mpg.rename(columns={"cty":"city"})

# Rename the hwy column to highway.
mpg.rename(columns={"hwy":"highway"})

# Do any cars have better city mileage than highway mileage?
comparison = mpg.cty > mpg.hwy
comparison

mpg[comparison]

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg["mileage_difference"] = mpg.hwy - mpg.cty
mpg.head()

# Which car (or cars) has the highest mileage difference?
mpg.sort_values(by="mileage_difference", ascending=False).head(2) #2 cars had difference of 12

# Which compact class car has the lowest highway mileage? The best?
mpg[mpg["class"] == "compact"].sort_values(by="hwy").head(1)
mpg[mpg["class"] == "compact"].sort_values(by="hwy", ascending=False).head(1)

# Create a column named average_mileage that is the mean of the city and highway mileage.
average_mileage = (mpg.cty+mpg.hwy)/2

mpg["average_mileage"] = average_mileage
mpg.head()

#david's solution for computing for average
mpg[['highway','city']].apply(np.mean, axis=1)

# Which dodge car has the best average mileage? The worst?

mpg[mpg.manufacturer == "dodge"].sort_values(by="average_mileage", ascending=False).head(1)
mpg[mpg.manufacturer == "dodge"].sort_values(by="average_mileage").head(1)

# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mammals = data("Mammals")
data('Mammals',show_doc=True)
# How many rows and columns are there?
mammals.shape
#107 rows, 4 columns

# What are the data types?
mammals.dtypes
#weight and speed are floats, hoppers and specials are booleans

# Summarize the dataframe with .info and .describe
mammals.info
mammals.describe()

# What is the the weight of the fastest animal?
mammals.sort_values(by="speed", ascending=False).head(1).weight

# What is the overal percentage of specials?
specials_true = mammals.specials.sum()
specials_false = mammals.specials.count() - specials_true

count_of_specials = specials_true + specials_false

percentage_of_special = (specials_true/count_of_specials)*100
percentage_of_non_special = (specials_false/count_of_specials)*100

print("The percentage of specials is",round(percentage_of_special,2), "%")

#alternative solutions
sum(mammals.specials==True)/len(mammals)*100
(mammals.specials==True).mean()*100

# How many animals are hoppers that are above the median speed? What percentage is this?
median_speed = mammals.speed.median()

hoppers_above_median = mammals[lambda x: mammals.hoppers][mammals.speed > median_speed].hoppers.count()
hoppers_above_median

round(hoppers_above_median/len(mammals)*100,2)

