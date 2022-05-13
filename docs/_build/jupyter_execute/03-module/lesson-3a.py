#!/usr/bin/env python
# coding: utf-8

# # Lesson 3a: Selecting and filtering

# > “Every second of every day, our senses bring in way too much data than we can possibly process in our brains.”
# >
# > \- Peter Diamandis, Founder of the X-Prize for human-AI collaboration
# 
# When performing data analysis tasks, rarely do we want to use _all_ our data. Often, we want to focus in on specific variables of interest and/or observations of interest. This requires us to be able to subset our DataFrame in various ways, which is the emphasis of this lesson.
# 
# ## Learning objectives
# 
# By the end of this lesson you'll be able to:
# 
# * Differentiate between the different ways to subset DataFrames.
# * Select columns of a DataFrame.
# * Slice and filter specific rows of a DataFrame.
# 
# ## Prerequisites
# 
# To illustrate selecting and filtering let's go ahead and load the pandas library and import some data:

# In[1]:


import pandas as pd

planes_df = pd.read_csv('../data/planes.csv')
planes_df.head()


# ## Subsetting dimensions
# 
# We don't always want all of the data in a DataFrame, so we need to take subsets of the DataFrame. In general, **subsetting** is extracting a small portion of a DataFrame -- making the DataFrame smaller. Since the DataFrame is two-dimensional, there are two dimensions on which to subset.
# 
# **Dimension 1:** We may only want to consider certain *variables*. For example, we may only care about the `year` and `engines` variables:
# 
# [![](../images/selecting_columns.png)](https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/selecting_columns.png?raw=true)
# 
# We call this **selecting** columns/variables -- this is similar to SQL's `SELECT` or R's dplyr package's `select()`.

# **Dimension 2:** We may only want to consider certain *cases*. For example, we may only care about the cases where the manufacturer is Embraer.
# 
# [![](../images/selecting_rows.png)](https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/selecting_rows.png?raw=true)
# 
# We call this **filtering** or **slicing** -- this is similar to SQL's `WHERE` or R's dplyr package's `filter()` or `slice()`. And we can combine these two options to subset in both dimensions -- the `year` and `engines` variables where the manufacturer is Embraer:
# 
# [![](../images/selecting_rows_columns.png)](https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/selecting_rows_columns.png?raw=true)

# In the previous example, we want to do two things using `planes_df`:
# 
#   1. **select** the `year` and `engines` variables
#   2. **filter** to cases where the manufacturer is Embraer
# 
# But we also want to return a new DataFrame -- not just highlight certain cells. In other words, we want to turn this:

# In[2]:


planes_df.head()


# Into this:

# In[3]:


planes_df.head().loc[planes_df['manufacturer'] == 'EMBRAER', ['year', 'engines']]


# So we really have a third need: return the resulting DataFrame so we can continue our analysis:
# 
#   1. **select** the `year` and `engines` variables
#   2. **filter** to cases where the manufacturer is Embraer
#   3. Return a DataFrame to continue the analysis

# ## Subsetting variables
# 
# Recall that the subsetting of variables/columns is called **selecting** variables/columns. In a simple example, we can select a single variable using bracket subsetting notation:
# 

# In[4]:


planes_df['year'].head()


# Notice the `head()` method also works on `planes_df['year']` to return the first five elements.

# ```{admonition} Question:
# :class: attention
# What is the data type of `planes_df['year']`?
# ```

# This returns `pandas.core.series.Series`, referred to simply as a "Series", rather than a DataFrame.

# In[5]:


type(planes_df['year'])


# This is okay -- the Series is a popular data structure in Python. Recall from a previous lesson:
# 
# * A Series is a one-dimensional data structure -- this is similar to a Python `list`
# * Note that all objects in a Series are usually of the same type (but this isn't a strict requirement)
# * Each DataFrame can be thought of as a list of equal-length Series (plus an Index)
# 
# <center>
# <img src="https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/dataframe-series.png?raw=true" alt="dataframe-series.png" width="300" height="300">
# </center>
# 
# Series can be useful, but for now, we are interested in *returning a DataFrame* rather than a series. We can select a single variable and return a DataFrame by still using bracket subsetting notation, but this time we will <span style="color: blue">pass a <u>`list`</u> of variables names</span>:

# In[6]:


planes_df[['year']].head()


# And we can see that we've returned a DataFrame:

# In[7]:


type(planes_df[['year']].head())


# ```{admonition} Question:
# :class: attention
# What's another advantage of this passing a `list`?
# ```
# 
# Passing a list into the bracket subsetting notation allows us to select multiple variables at once:

# In[8]:


planes_df[['year', 'engines']].head()


# In another example, assume we are interested in the `model` of plane, number of `seats` and `engine` type:

# In[9]:


planes_df[['model', 'seats', 'engine']].head()


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 
# 1. ______ is a common term for subsetting DataFrame variables.
# 2. What type of object is a DataFrame column?
# 3. What will be returned by the following code?
# 
#    ```python
#    planes_df['type', 'model']
#    ```

# ## Subsetting rows
# 
# When we subset rows (aka cases, records, observations) we primarily use two names: **slicing** and **filtering**, but *these are not the same*:
# 
#   * **slicing**, similar to row **indexing**, subsets observations by the value of the Index
#   * **filtering** subsets observations using a conditional test

# ### Slicing rows
# 
# Remember that all DataFrames have an Index:

# In[10]:


planes_df.head()


# We can **slice** cases/rows using the values in the Index and bracket subsetting notation. It's common practice to use `.loc` to slice cases/rows:

# In[11]:


planes_df.loc[0:5]


# ```{note}
# Note that since this is ***not*** "indexing", the last element is inclusive.
# ```
# 
# We can also pass a `list` of Index values:

# In[12]:


planes_df.loc[[0, 2, 4, 6, 8]]


# ### Filtering rows
# 
# We can **filter** rows using a logical sequence equal in length to the number of rows in the DataFrame.
# 
# Continuing our example, assume we want to determine whether each case's `manufacturer` is Embraer. We can use the `manufacturer` Series and a logical equivalency test to find the result for each row:

# In[13]:


planes_df['manufacturer'] == 'EMBRAER'


# We can use this resulting logical sequence to test **filter** cases -- rows that are `True` will be returned while those that are `False` will be removed:

# In[14]:


planes_df[planes_df['manufacturer'] == 'EMBRAER'].head()


# This also works with `.loc`:

# In[15]:


planes_df.loc[planes_df['manufacturer'] == 'EMBRAER'].head()


# Any conditional test can be used to **filter** DataFrame rows:

# In[16]:


planes_df.loc[planes_df['year'] > 2002].head()


# And multiple conditional tests can be combined using logical operators:

# In[17]:


planes_df.loc[(planes_df['year'] > 2002) & (planes_df['year'] < 2004)].head()


# ```{note}
# Note that each condition is wrapped in parentheses -- this is required.
# ```
# 
# Often, as your condition gets more complex, it can be easier to read if you separate out the condition:

# In[18]:


cond = (planes_df['year'] > 2002) & (planes_df['year'] < 2004)
planes_df.loc[cond].head()


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 
# 1. What's the difference between **slicing** cases and **filtering** cases?
# 2. Fill in the blanks to fix the following code to find planes that have more than three engines:
# 
#    ```python
#     planes_df.loc[______['______'] > 3]
#    ```

# ## Selecting variables and filtering rows
# 
# If we want to select variables and filter cases at the same time, we have a few options:
# 
# 1. Sequential operations
# 2. Simultaneous operations

# ### Sequential Operations
# 
# We can use what we've previously learned to select variables and filter cases in multiple steps:

# In[19]:


planes_df_filtered = planes_df.loc[planes_df['manufacturer'] == 'EMBRAER']
planes_df_filtered_and_selected = planes_df_filtered[['year', 'engines']]
planes_df_filtered_and_selected.head()


# This is a good way to learn how to select and filter independently, and it also reads very clearly.

# ### Simultaneous operations
# 
# However, we can also do both selecting and filtering in a single step with `.loc`:

# In[20]:


planes_df.loc[planes_df['manufacturer'] == 'EMBRAER', ['year', 'engines']].head()


# This option is more succinct and also reduces programming time. As before, as your filtering and selecting conditions get longer and/or more complex, it can make it easier to read to break it up into separate lines:

# In[21]:


rows = planes_df['manufacturer'] == 'EMBRAER'
cols = ['year', 'engines']
planes_df.loc[rows, cols].head()


# ### Knowledge check
# 
# ```{admonition} Question:
# :class: attention
# Subset `planes_df` to only include planes made by Boeing and the `seats` and `model` variables.
# ```

# ## Views vs copies
# 
# One thing to be aware of, as you will likely experience it eventually, is the concept of returning a ***view*** (“looking” at a part of an existing object) versus a ***copy*** (making a new copy of the object in memory). This can be a bit abstract and even [this section in the Pandas docs](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy) states _"...it’s very hard to predict whether it will return a view or a copy."_
# 
# ```{tip}
# The concept of views and copies is confusing and you can read more about it [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy). 
# ```
# 
# The main takeaway is that the most common warning you’ll encounter in Pandas is the `SettingWithCopyWarning`; Pandas raises it as a warning that you might not be doing what you think you’re doing or because the operation you are performing may behave unpredictably.
# 
# Let's look at an example. Say the number of seats on this particular plane was recorded incorrectly. Instead of 55 seats it should actually be 60 seats.

# In[22]:


tailnum_of_interest = planes_df['tailnum'] == 'N10156'
planes_df[tailnum_of_interest]


# Instead of using `.iloc`, we could actually filter and select this element in our DataFrame with the following bracket notation.

# In[23]:


planes_df[tailnum_of_interest]['seats']


# If we use this approach to then assign our new value to this element we'll get a `SettingWithCopyWarning`.

# In[24]:


planes_df[tailnum_of_interest]['seats'] = 60


# So what's going on? Did our DataFrame get changed?

# In[25]:


planes_df[tailnum_of_interest]


# No it didn’t, even though you probably thought it did. What happened above is that `planes_df[tailnum_of_interest]['seats']` was executed first and returned a copy of the DataFrame, which is an entirely different object. We can confirm by using `id()`:

# In[26]:


print(f"The id of the original dataframe is: {id(planes_df)}")
print(f" The id of the indexed dataframe is: {id(planes_df[tailnum_of_interest])}")


# We then tried to set a value on this new object by appending `['seats'] = 60`. Pandas is warning us that we are doing that operation on a copy of the original dataframe, which is probably not what we want. To fix this, you need to index in a single go, using `.loc[]` for example:
# 

# In[27]:


planes_df.loc[tailnum_of_interest, 'seats'] = 60


# No error this time! And let’s confirm the change:

# In[28]:


planes_df[tailnum_of_interest]


# ```{tip}
# When in doubt, always use `.loc[]` for combined filtering and selecting!
# ```

# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# 1. Import the heart.csv
# 2. Select the age column and return a Series. Select the age column and return a DataFrame. Select the age, sex, and max_hr columns.
# 3. Slice the DataFrame to get the first 25 rows and save as `first_25`. What is the age of the last observation in this sliced DataFrame?
# 4. Using the original DataFrame (not the sliced DataFrame), filter for all observations where the person is 50 years or older. How many observations are there?
# 5. Using the original DataFrame, filter for those observations that are male and 50 years or older. How many observations are there.
# 6. Using the original DataFrame, filter for those observations that are female, 50 years or younger, and have the disease (disease = 1). Select `chest_pain`, `chol`, and `max_hr` columns. How many rows and columns are in the resulting DataFrame?
# ```
