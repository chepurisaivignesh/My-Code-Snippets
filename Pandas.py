import pandas as pd

a = [1, 7, 2]
myvari = pd.Series(a)
print(myvari)
print(myvari[0])

print("##################################################")

aa = [1, 7, 2]
myvaria = pd.Series(aa, index = ["x", "y", "z"])
print(myvaria)
print(myvaria['y'])

print("##################################################")

calories = {"day1": 420, "day2": 380, "day3": 390}
myvariab = pd.Series(calories)
print(myvariab)
print(myvariab['day1'])

print("##################################################")

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvariabl = pd.DataFrame(data)
print(myvariabl)
print(myvariabl.loc[0])#loc=Locate row, This example returns pandas series
# print(type(myvariabl.loc[0]))
print(myvariabl.loc[[0, 1]]) #the result is a Pandas DataFrame
# print(type(myvariabl.loc[[0, 1]]))
# Note: When using [], the result is a Pandas DataFrame.

print("##################################################")

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 

print("##################################################")

#Reading csv files
# df = pd.read_csv('data.csv')
# print(df) 

print("##################################################")

df = pd.read_csv('pandas sample data.csv') 
#Tip: use to_string() to print the entire DataFrame.
print(df.to_string())

print("##################################################")

dff = pd.read_csv('pandas sample data.csv')
# By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows
print(dff) 

print("##################################################")

dfm = pd.read_csv('pandas sample data.csv')

# The head() method returns the headers and a specified number of rows, starting from the top.
# if the number of rows is not specified, the head() method will return the top 5 rows.
# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, starting from the bottom.
# The DataFrames object has a method called info(), that gives you more information about the data set.

print(dfm.head(10))
print(dfm.tail()) 
print(dfm.info()) 

#In this example:

# The result tells us there are 169 rows and 4 columns:

#   RangeIndex: 169 entries, 0 to 168
#   Data columns (total 4 columns):

# And the name of each column, with the data type:

#    #   Column    Non-Null Count  Dtype  
#   ---  ------    --------------  -----  
#    0   Duration  169 non-null    int64  
#    1   Pulse     169 non-null    int64  
#    2   Maxpulse  169 non-null    int64  
#    3   Calories  164 non-null    float64

# Null Values
# The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data.

print("##################################################")

# Data cleaning means fixing bad data in your data set.

# Bad data could be:

# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

# If you want to change the original DataFrame, use the "inplace = True" argument

dfo = pd.read_csv('pandas sample data.csv')
new_df = dfo.dropna() #Return a new Data Frame with no empty cells
print(new_df.to_string())

# Now, the "dropna(inplace = True)" will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.
dfk = pd.read_csv('pandas sample data.csv')
dfk.dropna(inplace = True)
print(dfk.to_string())

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value
# Ex:Replace NULL values with the number 130

dfv = pd.read_csv('pandas sample data.csv')
dfv.fillna(130, inplace = True)

# Replace Only For Specified Columns
# The example above replaces all empty cells in the whole Data Frame.
# To only replace empty values for one column, specify the column name for the DataFrame:
# Ex:Replace NULL values in the "Calories" columns with the number 130

dfh = pd.read_csv('data.csv')
dfh["Calories"].fillna(130, inplace = True)

# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
# Ex:Calculate the MEAN, and replace any empty values with it

dfj = pd.read_csv('data.csv')
x = dfj["Calories"].mean()
dfj["Calories"].fillna(x, inplace = True)

# Ex: Calculate the MEDIAN, and replace any empty values with it

df = pd.read_csv('data.csv')
xb = df["Calories"].median()
df["Calories"].fillna(xb, inplace = True)

# Ex:Calculate the MODE, and replace any empty values with it

dfa = pd.read_csv('data.csv')
xa = df["Calories"].mode()[0]
dfa["Calories"].fillna(xa, inplace = True)

print("##############################################################")

# Let's try to convert all cells in the 'Date' column into dates.
# Pandas has a to_datetime() method for this:
# Ex : Convert to date:

dfq = pd.read_csv('data.csv')
dfq['Date'] = pd.to_datetime(dfq['Date']) # 20201226>>>>2020/12/26
print(dfq.to_string())

print("###############################################################")

# Removing Rows
# The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.
# In this example Ex:
# Remove rows with a NULL value in the "Date" column

dfq.dropna(subset=['Date'], inplace = True)

print("###############################################################")

# Replacing Values
# One way to fix wrong values is to replace them with something else.
# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
# Ex:Set "Duration" = 45 in row 7:

dfq.loc[7, 'Duration'] = 45

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.
# Ex:Loop through all values in the "Duration" column.If the value is higher than 120, set it to 120:

for x in dfq.index:
  if dfq.loc[x, "Duration"] > 120:
    dfq.loc[x, "Duration"] = 120

# Removing Rows
# Another way of handling wrong data is to remove the rows that contains wrong data.
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
# Ex: Delete rows where "Duration" is higher than 120

for x in dfq.index:
  if dfq.loc[x, "Duration"] > 120:
    dfq.drop(x, inplace = True)

# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:
# Ex: Returns True for every row that is a duplicate, othwerwise False:

print(dfq.duplicated())

# The above example result is:
#      Duration          Date  Pulse  Maxpulse  Calories
#   0         60  '2020/12/01'    110       130     409.1
#   1         60  '2020/12/02'    117       145     479.0
#   2         60  '2020/12/03'    103       135     340.0
#   3         45  '2020/12/04'    109       175     282.4
#   4         45  '2020/12/05'    117       148     406.0
#   5         60  '2020/12/06'    102       127     300.0
#   6         60  '2020/12/07'    110       136     374.0
#   7        450  '2020/12/08'    104       134     253.3
#   8         30  '2020/12/09'    109       133     195.1
#   9         60  '2020/12/10'     98       124     269.0
#   10        60  '2020/12/11'    103       147     329.3
#   11        60  '2020/12/12'    100       120     250.7
#   12        60  '2020/12/12'    100       120     250.7
#   13        60  '2020/12/13'    106       128     345.3
#   14        60  '2020/12/14'    104       132     379.3
#   15        60  '2020/12/15'     98       123     275.0
#   16        60  '2020/12/16'     98       120     215.2
#   17        60  '2020/12/17'    100       120     300.0
#   18        45  '2020/12/18'     90       112       NaN
#   19        60  '2020/12/19'    103       123     323.0
#   20        45  '2020/12/20'     97       125     243.0
#   21        60  '2020/12/21'    108       131     364.2
#   22        45           NaN    100       119     282.0
#   23        60  '2020/12/23'    130       101     300.0
#   24        45  '2020/12/24'    105       132     246.0
#   25        60  '2020/12/25'    102       126     334.5
#   26        60      20201226    100       120     250.0
#   27        60  '2020/12/27'     92       118     241.0
#   28        60  '2020/12/28'    103       132       NaN
#   29        60  '2020/12/29'    100       132     280.0
#   30        60  '2020/12/30'    102       129     380.3
#   31        60  '2020/12/31'     92       115     243.0

# Removing Duplicates
# To remove duplicates, use the drop_duplicates() method.
# Ex:Remove all duplicates

dfq.drop_duplicates(inplace = True)

# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.

# Finding Relationships
# A great aspect of the Pandas module is the corr() method.
# The corr() method calculates the relationship between each column in your data set.
# Ex: Show the relationship between the columns

dfq.corr()

# Note: The corr() method ignores "not numeric" columns.

# Result Explained
# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

# The number varies from -1 to 1.

# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

# 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

# -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

# 0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

# What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.

# Perfect Correlation:
# We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has a perfect relationship with itself.

# Good Correlation:
# "Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.

# Bad Correlation:
# "Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.

# Plotting
# Pandas uses the plot() method to create diagrams.
# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
# Ex: Import pyplot from Matplotlib and visualize our DataFrame:

import matplotlib.pyplot as plt

df = pd.read_csv('pandas sample data.csv')
df.plot()
plt.show()

# Scatter Plot
# Specify that you want a scatter plot with the kind argument:
# kind = 'scatter'
# A scatter plot needs an x- and a y-axis.
# In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.
# Include the x and y arguments like this: x = 'Duration', y = 'Calories'

df = pd.read_csv('data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

# Histogram
# Use the kind argument to specify that you want a histogram:
# kind = 'hist'
# A histogram needs only one column.
# A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
# In the example below we will use the "Duration" column to create the histogram

df["Duration"].plot(kind = 'hist')