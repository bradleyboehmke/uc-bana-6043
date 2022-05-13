#!/usr/bin/env python
# coding: utf-8

# # Summarizing Data
# 
# > What we have is a data glut.
# >
# > \- Vernor Vinge, Professor Emeritus of Mathematics, San Diego State University

# ## Applied Review

# ### Dictionaries

# * The `dict` structure is used to represent **key-value pairs**

# * Like a real dictionary, you look up a word (**key**) and get its definition (**value**)

# * Below is an example:
# 
# ```python
# ethan = {
#     'first_name': 'Ethan',
#     'last_name': 'Swan',
#     'alma_mater': 'Notre Dame',
#     'employer': '84.51˚',
#     'zip_code': 45208
# }
# ```

# ### DataFrame Structure

# * We will start by importing the `flights` data set as a DataFrame:

# In[1]:


import pandas as pd
flights_df = pd.read_csv('../data/flights.csv')


# * Each DataFrame variable is a **Series** and can be accessed with bracket subsetting notation: `DataFrame['SeriesName']`

# * The DataFrame has an **Index** that is visible the far left side and can be used to slice the DataFrame

# ### Methods

# * Methods are *operations* that are specific to Python classes

# * These operations end in parentheses and *make something happen*

# * An example of a method is `DataFrame.head()`

# ## General Model

# ### Window Operations

# Yesterday we learned how to manipulate data across one or more variables within the row(s):
# 
# <img src="images/series-plus-series.png" alt="series-plus-series.png" width="80%" height="80%">

# <div class="admonition note alert alert-info">
#     <b><p class="first admonition-title" style="font-weight: bold">Note</p></b>
#     <p>We return the same number of elements that we started with. This is known as a <b>window function</b>, but you can also think of it as summarizing at the row-level.</p>
# </div>

# We could achieve this result with the following code:
# 
# ```python
# DataFrame['A'] + DataFrame['B']
# ```

# We subset the two Series and then add them together using the `+` operator to achieve the sum.

# Note that we could also use some other operation on `DataFrame['B']` as long as it returns the same number of elements.

# ### Summary Operations

# However, sometimes we want to work with data across rows within a variable -- that is, aggregate/summarize values rowwise rather than columnwise.

# <img src="images/aggregate-series.png" alt="aggregate-series.png" width="50%" height="50%">

# <div class="admonition note alert alert-info">
#     <b><p class="first admonition-title" style="font-weight: bold">Note</p></b>
#     <p>We return a single value representing some aggregation of the elements we started with. This is known as a <b>summary function</b>, but you can think of it as summarizing across rows.</p>
# </div>

# This is what we are going to talk about next.

# ## Summarizing a Series

# ### Summary Methods

# The easiest way to summarize a specific series is by using bracket subsetting notation and the built-in Series methods (i.e. `col.sum()`):

# In[2]:


flights_df['distance'].sum()


# Note that a *single value* was returned because this is a **summary operation** -- we are summing the `distance` variable across all rows.

# There are other summary methods with a series:

# In[3]:


flights_df['distance'].mean()


# In[4]:


flights_df['distance'].median()


# In[5]:


flights_df['distance'].std()


# All of the above methods work on quantitative variables but not character variables. However, there are summary methods that will work on all types of variables:

# In[6]:


# Number of unique values in the carrier variable
flights_df['carrier'].nunique()


# In[7]:


# Most frequent value observed in the carrier variable
flights_df['carrier'].mode()


# <font class="your_turn">
#     Your Turn
# </font>
# 
# 1\. What is the difference between a window operation and a summary operation?
# 
# 2\. Fill in the blanks in the following code to calculate the mean delay in departure:
# 
#    ```python
#    flights_df['_____']._____()
#    ```
# 
# 
# 3\. Find the count of each value observed in the carriers column. This may take a Google search. Would you consider the output a summary operation?

# ### Describe Method

# There is also a method `describe()` that provides a lot of this summary information -- this is especially useful in initial exploratory data analysis.

# In[8]:


flights_df['distance'].describe()


# <div class="admonition note alert alert-info">
#     <b><p class="first admonition-title" style="font-weight: bold">Note</p></b>
#     <p>The <tt class=\"docutils literal\">describe()</tt> method will return different results depending on the <tt class=\"docutils literal\">type</tt> of the Series.</p>
# </div>

# In[9]:


flights_df['carrier'].describe()


# ## Summarizing a DataFrame

# The above methods and operations are nice, but sometimes we want to work with multiple variables rather than just one.

# ### Extending Summary Methods to DataFrames

# Recall how we select variables from a DataFrame:

# * Single-bracket subset notation

# * Pass a list of quoted variable names into the list

# ```python
# flights_df[['sched_dep_time', 'dep_time']]
# ```

# We can use *the same summary methods from the Series on the DataFrame* to summarize data:

# In[10]:


flights_df[['sched_dep_time', 'dep_time']].mean()


# In[11]:


flights_df[['sched_dep_time', 'dep_time']].median()


# <div class="admonition tip alert alert-warning">
#     <b><p class="first admonition-title" style="font-weight: bold">Question</p></b>
#     <p>What is the type of...<br> <tt class=\"docutils literal\">flights_df[['sched_dep_time', 'dep_time']].median()</tt>?</p>
# </div>

# This returns a `pandas.core.series.Series` object  -- the Index is the variable name and the values are the summarized values.

# ### The Aggregation Method

# While summary methods can be convenient, there are a few drawbacks to using them on DataFrames:

# 1. You have to look up or remember the method names each time
# 2. You can only apply one summary method at a time
# 3. You have to apply the same summary method to all variables
# 4. A Series is returned rather than a DataFrame -- this makes it difficult to use the values in our analysis later

# In order to get around these problems, the DataFrame has a powerful method `agg()`:

# In[12]:


flights_df.agg({
    'sched_dep_time': ['mean']
})


# There are a few things to notice about the `agg()` method:

# 1. A `dict` is passed to the method with variable names as keys and a list of quoted summaries as values

# 2. *A DataFrame is returned* with variable names as variables and summaries as rows

# <div class="admonition tip alert alert-warning">
#     <b><p class="first admonition-title" style="font-weight: bold">Tip!</p></b>
#     <p>The <tt class=\"docutils literal\">.agg()</tt> method is just shorthand for <tt class=\"docutils literal\">.aggregate()</tt>.</p>
# </div>

# In[13]:


# I'm feeling quite verbose today!
flights_df.aggregate({
    'sched_dep_time': ['mean']
})


# In[14]:


# I don't have that kind of time!
flights_df.agg({
    'sched_dep_time': ['mean']
})


# We can extend this to multiple variables by adding elements to the `dict`:

# In[15]:


flights_df.agg({
    'sched_dep_time': ['mean'],
    'dep_time': ['mean']
})


# And because the values of the `dict` are lists, we can do additional aggregations at the same time:

# In[16]:


flights_df.agg({
    'sched_dep_time': ['mean', 'median'],
    'dep_time': ['mean', 'min']
})


# <div class="admonition note alert alert-info">
#     <b><p class="first admonition-title" style="font-weight: bold">Note</p></b>
#     <p>Not all variables have to have the same list of summaries.</p>
# </div>

# <font class="your_turn">
#     Your Turn
# </font>

# 1\. What class of object is the returned by the below code?
# 
# ```python
# flights_df[['air_time', 'distance']].mean()
# ```

# 2\. What class of object is returned by the below code?
# 
# ```python
# flights_df.agg({
#     'air_time': ['mean'],
#     'distance': ['mean']
# })
# ```

# 3\. Fill in the blanks in the below code to calculate the minimum and maximum distances traveled and the mean and median arrival delay:
# 
# ```python
# flights_df.agg({
#     '_____': ['min', '_____'],
#     '_____': ['_____', 'median']
# })
# ```

# ### Describe Method

# While `agg()` is a powerful method, the `describe()` method -- similar to the Series `describe()` method -- is a great choice during exploratory data analysis:

# In[17]:


flights_df.describe()


# <font class="question">
#     <strong>Question</strong>:<br><em>What is missing from the above result?</em>
# </font>

# The string variables are missing!

# We can make `describe()` compute on all variable types using the `include` parameter and passing a list of data types to include:

# In[18]:


flights_df.describe(include = ['int', 'float', 'object'])


# ## Questions
# 
# Are there any questions before we move on?
