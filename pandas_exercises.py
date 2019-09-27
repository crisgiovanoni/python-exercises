from pydataset import data

mpg = data('mpg', show_doc=True)
mpg = data('mpg')
mpg

#data overview
mpg.head(1)

# On average, which manufacturer has the best miles per gallon?

average_mpg = (mpg.hwy + mpg.cty)/2
mpg["average_mpg"] = average_mpg

mpg.sort_values(by="average_mpg", ascending=False).head(1)

# How many different manufacturers are there?

manufacturer_group = mpg.groupby("manufacturer").count()
manufacturer_group = manufacturer_group.reset_index()

manufacturer_group.manufacturer.count()

# How many different models are there?

manufacturer_group.model.sum()

# Do automatic or manual cars have better miles per gallon?

#Step 1: add a column that contains only auto and manual
def transition_category(series):
    for x in series:
        if x in "auto":
            return "auto"
        else:
            return "manual"

type(mpg.trans)

transition = mpg.trans.apply(transition_category)

mpg["transition"] = transition

#Step 2: group by transition column and aggregate mean by average_mpg

mpg.groupby("transition").average_mpg.agg("mean")

# Joining and Merging
# Copy the users and roles dataframes from the examples above.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# What do you think a right join would look like?
# Answer: A row with the commenter role is added even if there's no user filling that role in.


pd.merge(
    users.rename(columns={'id': 'user_id', 'name': 'username'}), 
    roles.rename(columns={'name': 'role_name'}),
    left_on='role_id', right_on='id',
    how='right')
    

# An outer join?
# Answer: it joined the observations that match, and kept the observations that don't 
pd.merge(
    users.rename(columns={'id': 'user_id', 'name': 'username'}), 
    roles.rename(columns={'name': 'role_name'}),
    left_on='role_id', right_on='id',
    how='outer')

# What happens if you drop the foreign keys from the dataframes and try to merge them?
# Answer: returns no observation
users_without_index = users.drop(columns="id")
roles_without_index = users.drop(columns="id")

pd.merge(users,roles)

# Getting data from SQL databases

# Create a function named get_db_url.
# It should accept a username, hostname, password, and database name and return a url formatted
# like in the examples in this lesson.

def get_db_url(u,p,h,d):
    url = f'mysql+pymysql://{u}:{p}@{h}/{d}'
    return url

# Use your function to obtain a connection to the employees database.
from env import host, user, password

host = host
user = user
password = password

url = get_db_url(host,password,host,"employees")
url


# Once you have successfully run a query:
# Intentionally make a typo in the database url. What kind of error message do you see?

url = get_db_url(host,password,host,"employee")

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)

# Intentionally make an error in your SQL query. What does the error message look like?
# Answer: Operational error, access denied

# Read the employees and titles tables into two separate dataframes

employees_df = pd.read_sql('SELECT * FROM employees',url)
titles_df = pd.read_sql('SELECT * FROM titles',url)

employees_df.head(5)
titles_df.head(5)

# Visualize the number of employees with each title.

titles_df.groupby("title").title.count()

# Join the employees and titles dataframes together.

employees_with_titles = pd.merge(
    employees_df,titles_df,
    left_on="emp_no",
    right_on="emp_no",
    how="left"
    )

# Visualize how frequently employees change titles.

employees_with_titles.groupby("emp_no").agg("sum", axis="title").head(20)

# For each title, find the hire date of the employee that was hired most recently with that title.

employees_with_titles.dtypes

#hire_date is an object(string) type, so first, convert the hire_date into a date type

pd.to_datetime(employees_with_titles.hire_date)

employees_with_titles.groupby("title").agg("max", axis="hire_date").head(5)

# Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL and python/pandas code)

# Join Title, Dept_Emp, Departments Table 

sql_selection = """
SELECT *
FROM titles as t
JOIN dept_emp as de
	ON t.emp_no = de.emp_no
JOIN departments as d
	ON d.dept_no = de.dept_no
"""

departments_with_title = pd.read_sql(sql_selection, url)

pd.crosstab(departments_with_title.title, departments_with_title.dept_name)

# Use your get_db_url function to help you explore the data from the chipotle database. Use the data to answer the following questions:


chipotle_url = get_db_url("bayes_819","JH4OscOawDom6Kq29wWZQuOQXzxrWYmx","157.230.209.171","chipotle")

chipotle = pd.read_sql('SELECT * FROM orders', chipotle_url)

chipotle.item_price = chipotle.item_price.str.replace("$","").astype(float)

chipotle.head(1)
# What is the total price for each order?
chipotle.dtypes

chipotle.groupby("order_id").agg("sum", axis="item_price").head(5)

# What are the most popular 3 items?
#sort item name by frequency

chipotle.groupby("item_name").agg("count").tail(5)

# Which item has produced the most revenue?

chipotle.groupby("item_name").agg("sum", axis="item_price").sort_values(by="item_price",ascending=False).head(1)