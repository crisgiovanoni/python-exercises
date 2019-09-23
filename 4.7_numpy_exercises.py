import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?

negatives_in_a = a[a < 0]
print(len(negatives_in_a))

# How many positive numbers are there?

positives_in_a = a[a > 0]
print(len(positives_in_a))

# How many even positive numbers are there?

evens_in_a = a[a % 2 == 0]
print(evens_in_a)

np.intersect1d(positives_in_a, evens_in_a)

# If you were to add 3 to each data point, how many positive numbers would there be?

plus_3 = a + 3
print(plus_3)

len(plus_3[plus_3 > 0])

# If you squared each number, what would the new mean and standard deviation be?

squared_a = a ** 2
squared_a.mean()
squared_a.std()

# A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.
a.mean() # see what mean is
centered_a = a - (a.mean())
print(centered_a)

# Calculate the z-score for each data point. Recall that the z-score is given by:
zscores_of_a = centered_a/a.std()
print(zscores_of_a)