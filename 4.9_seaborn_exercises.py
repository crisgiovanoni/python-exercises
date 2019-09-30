import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pydataset import data
iris = data("iris")

iris = data("iris", show_doc=True) #viewing iris docs
iris.columns #viewing column_names

# What does the distribution of petal lengths look like?
sns.distplot(iris["Petal.Length"])

# Is there a correlation between petal length and petal width?
iris_corr = iris.corr() #check contingency tables
petal_lengthwidth = pd.crosstab(iris_corr["Petal.Length"], iris_corr["Petal.Width"])

sns.heatmap(petal_lengthwidth,annot=False)

# Would it be reasonable to predict species based on sepal width and sepal length?
# Which features would be best used to predict species?

sns.relplot(x="Sepal.Length",y="Sepal.Width",data=iris,hue="Species")

sepals_corr = pd.crosstab(iris["Sepal.Length"], iris["Sepal.Width"], normalize=True)
sepals_corr
sns.heatmap(sepals_corr)

### ANSCOMBE ###
# Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set.
# Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?
anscombe = sns.load_dataset("anscombe")
type(anscombe)

anscombe_group = anscombe.groupby("dataset").agg("count")
anscombe_group
anscombe.describe()

# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.
anscombe.columns
sns.relplot(x="x", y="y",col="dataset",data=anscombe)

# Load the InsectSprays dataset and read it's documentation.
# Create a boxplot that shows the effectiveness of the different insect sprays.

insect_sprays = data("InsectSprays")
insect_sprays = data("InsectSprays",show_doc=True)

insect_sprays.columns
sns.boxplot(data=insect_sprays,y="count",x="spray")

# Load the swiss dataset and read it's documentation. Create visualizations to answer the following questions:

swiss = data("swiss",show_doc=True)
swiss = data("swiss")
swiss.columns

swiss.head(1) #checking columns

# Create an attribute named is_catholic that holds a boolean value
# of whether or not the province is Catholic.
# (Choose a cutoff point for what constitutes catholic)
df["passing_math"] = df.math > 70
swiss["is_catholic"] = swiss["Catholic"] > 50

# Does whether or not a province is Catholic influence fertility?

swiss_corr = pd.crosstab(swiss["Fertility"],swiss["is_catholic"])
sns.heatmap(swiss_corr)

# What measure correlates most strongly with fertility?

correlation_swiss = swiss.corr()
correlation_swiss = correlation_swiss.drop(columns=["Fertility","is_catholic"])
correlation_swiss = correlation_swiss.head(1)
correlation_swiss
sns.heatmap(correlation_swiss)

# Using the chipotle dataset from the previous exercise
# create a bar chart that shows the 4 most popular items and the revenue produced by each.

def get_db_url(u,p,h,d):
    url = f'mysql+pymysql://{u}:{p}@{h}/{d}'
    return url

from env import host, user, password

host = host
user = user
password = password

chipotle_url = get_db_url(user,password,host,"chipotle")
chipotle_url
chipotle = pd.read_sql('SELECT * FROM orders', chipotle_url)

chipotle.columns

chipotle.item_price = chipotle.item_price.str.replace("$","").astype(float)

most_orders = chipotle.groupby("item_name").agg({"id":"count","item_price":"sum"})
most_orders
type(most_orders)
most_orders.sort_values(by="id",ascending=False)

top_four_items = most_orders.sort_values(by="id",ascending=False).head(4)
top_four_items
sns.barplot(x="id",y="item_price",data=top_four_items)

# Load the sleepstudy data and read it's documentation.
# Use seaborn to create a line chart of all the individual subject's reaction times
# and a more prominant line showing the average change in reaction time.

sleepstudy = data("sleepstudy")

sns.lineplot(x="Days", y="Reaction",hue="Subject",data=sleepstudy)
plt.hlines(sleepstudy["Reaction"].mean(), 0, 10, ls=':')