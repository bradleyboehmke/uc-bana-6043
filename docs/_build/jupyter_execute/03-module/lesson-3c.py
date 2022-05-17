#!/usr/bin/env python
# coding: utf-8

# # Lesson 3c: Summarizing data
# 
# > What we have is a data glut.
# >
# > \- Vernor Vinge, Professor Emeritus of Mathematics, San Diego State University
# 
# Computing summary statistics across columns and various groupings within your dataset is a fundamental task in creating insights from your data. This lesson will focus on how we can compute various aggregations with Pandas Series and DataFrames. 

# ## Learning objectives
# 
# By the end of this lesson you will be able to:
# 
# - Compute summary statistics across an entire Series
# - Compute summary statistics across one or more columns in a DataFrame
# - Compute grouped-level summary statistics across one or more columns in a DataFrame

# ## Simple aggregation
# 
# In the previous lesson we learned how to manipulate data across one or more variables within the row(s):
# 
# <center>
# <img src="https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/series-plus-series.png?raw=true" alt="series-plus-series.png" width="60%" height="60%">
# </center>
# 
# ```{note}
# We return the same number of elements that we started with. This is known as a **window function**, but you can also think of it as summarizing at the row-level.
# ```
# 
# We could achieve this result with the following code:
# 
# ```python
# DataFrame['A'] + DataFrame['B']
# ```
# 
# We subset the two Series and then add them together using the `+` operator to achieve the sum. Note that we could also use some other operation on `DataFrame['B']` as long as it returns the same number of elements.
# 
# However, sometimes we want to work with data across rows within a variable -- that is, aggregate/summarize values rowwise rather than columnwise.
# 
# <center>
# <img src="https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/aggregate-series.png?raw=true" alt="aggregate-series.png" width="50%" height="50%">
# </center>
# 
# ```{note}
# We return a single value representing some aggregation of the elements we started with. This is known as a **summary function**, but you can think of it as aggregating values across rows.
# ```

# ### Summarizing a series
# 
# The easiest way to summarize a specific series is by using bracket subsetting notation and the built-in Series methods (i.e. `col.sum()`):

# In[1]:


import pandas as pd

ames = pd.read_csv('../data/ames_raw.csv')

ames['SalePrice'].sum()


# Note that a *single value* was returned because this is a **summary operation** -- we are summing the `SalePrice` variable across all rows.
# 
# There are other summary methods with a series:

# In[2]:


ames['SalePrice'].mean()


# In[3]:


ames['SalePrice'].median()


# In[4]:


ames['SalePrice'].std()


# All of the above methods work on quantitative variables but not character variables. However, there are summary methods that will work on all types of variables:

# In[5]:


# Number of unique values in the neighborhood variable
ames['Neighborhood'].nunique()


# In[6]:


# Most frequent value observed in the neighborhood variable
ames['Neighborhood'].mode()


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. What is the difference between a window operation and a summary operation?
# 2. What is the mean, median, and standard deviation of the above ground square footage (`Gr Liv Area` variable)?  
# 3. Find the count of each value observed in the `Neighborhood` column. This may take a Google search. Would you consider the output a summary operation?
# ```

# ### Describe method
# 
# There is also a method `describe()` that provides a lot of this summary information -- this is especially useful in initial exploratory data analysis.

# In[7]:


ames['SalePrice'].describe()


# ```{note}
# The `describe()` method will return different results depending on the `type` of the Series.
# ```

# In[8]:


ames['Neighborhood'].describe()


# ### Summarizing a DataFrame
# 
# The above methods and operations are nice, but sometimes we want to work with multiple variables rather than just one. Recall how we select variables from a DataFrame:
# 
# * Single-bracket subset notation
# * Pass a list of quoted variable names into the list
# 
# ```python
# ames[['SalePrice', 'Gr Liv Area']]
# ```
# 
# We can use *the same summary methods from the Series on the DataFrame* to summarize data:

# In[9]:


ames[['SalePrice', 'Gr Liv Area']].mean()


# In[10]:


ames[['SalePrice', 'Gr Liv Area']].median()


# This returns a `pandas.core.series.Series` object  -- the Index is the variable name and the values are the summarized values.

# ### The Aggregation method
# 
# While summary methods can be convenient, there are a few drawbacks to using them on DataFrames:
# 
# 1. You can only apply one summary method at a time
# 2. You have to apply the same summary method to all variables
# 3. A Series is returned rather than a DataFrame -- this makes it difficult to use the values in our analysis later
# 
# In order to get around these problems, the DataFrame has a powerful method `.agg()`:

# In[11]:


ames.agg({
    'SalePrice': ['mean']
})


# There are a few things to notice about the `agg()` method:
# 
# 1. A `dict` is passed to the method with variable names as keys and a list of quoted summaries as values
# 2. *A DataFrame is returned* with variable names as variables and summaries as rows
# 
# ```{tip}
# The `.agg()` method is just shorthand for `.aggregate()`.
# ```

# In[12]:


# I'm feeling quite verbose today!
ames.aggregate({
    'SalePrice': ['mean']
})


# In[13]:


# I don't have that kind of time!
ames.agg({
    'SalePrice': ['mean']
})


# We can extend this to multiple variables by adding elements to the `dict`:

# In[14]:


ames.agg({
    'SalePrice': ['mean'],
    'Gr Liv Area': ['mean']
})


# And because the values of the `dict` are lists, we can do additional aggregations at the same time:

# In[15]:


ames.agg({
    'SalePrice': ['mean', 'median'],
    'Gr Liv Area': ['mean', 'min']
})


# ```{note}
# Not all variables have to have the same list of summaries. Note how `NaN` values fill in for those summary statistics _not_ computed on a given variable.
# ```

# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. Fill in the blanks to compute the average number of rooms above ground (`TotRms AbvGrd`) and the average number of bedrooms above ground (`Bedroom AbvGr`). What type of object is returned?
# 
#    ```python
#    ames[['______', '______']].______()
# 
# 2. Use the `.agg()` method to complete the same computation as above. How does the output differ?
# 3. Fill in the blanks in the below code to calculate the minimum and maximum year built (`Year Built`) and the mean and median number of garage stalls (`Garage Cars`):
# 
#    ```python
#    ames.agg({
#        '_____': ['min', '_____'],
#        '_____': ['_____', 'median']
#    })
# 
# ```

# ### Describe method
# 
# While `agg()` is a powerful method, the `describe()` method -- similar to the Series `describe()` method -- is a great choice during exploratory data analysis:

# In[16]:


ames.describe()


# ```{warning}
# What is missing from the above result?
# ```
# 
# The string variables are missing! We can make `describe()` compute on all variable types using the `include` parameter and passing a list of data types to include:

# In[17]:


ames.describe(include = ['int', 'float', 'object'])


# ## Grouped aggregation
# 
# In the section above, we talked about **summary** operations in the context of collapsing a DataFrame to a single row. This is not always the case -- often we are interested in examining specific groups in our data and we want to perform summary operations for these groups. Thus, we are interested in collapsing to a *single row per group*. This is known as a **grouped aggregation**.
# 
# For example, in the following illustration we are interested in finding the sum of variable `B` for each category/value in variable `A`.
# 
# <center>
# <img src="https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/summarizing-by-groups.png?raw=true" alt="summarizing-by-groups.png" width="80%" height="80%">
# </center>
# 
# This can be useful when we want to aggregate by category:
#   * Maximum temperature *by month*
#   * Total home runs *by team*
#   * Total sales *by neighborhood*
#   * Average number of seats *by plane manufacturer*
# 
# When we summarize by groups, we can use the same aggregation methods we previously did
#   * Summary methods for a specific summary operation: `DataFrame.sum()`
#   * Describe method for a collection of summary operations: `DataFrame.describe()`
#   * Agg method for flexibility in summary operations: `DataFrame.agg({'VariableName': ['sum', 'mean']})`
# 
# The only difference is the need to **set the DataFrame group prior to aggregating**. We can set the DataFrame group by calling the `DataFrame.groupby()` method and passing a variable name:

# In[18]:


ames_grp = ames.groupby('Neighborhood')
ames_grp


# Notice that a DataFrame doesn't print when it's grouped. The `groupby()` method is just setting the group - you can see the changed DataFrame class:

# In[19]:


type(ames_grp)


# The groupby object is really just a dictionary of index-mappings, which we could look at if we wanted to:

# In[20]:


ames_grp.groups


# We can also access a group using the `.get_group()` method:

# In[21]:


# get the Bloomington neighborhood group
ames_grp.get_group('Blmngtn').head()


# If we then call an aggregation method after our `groupby()` call, we will see the DataFrame returned with group-level aggregations:

# In[22]:


ames.groupby('Neighborhood').agg({'SalePrice': ['mean', 'median']}).head()


# This process always follows this model:
# 
# <center>
# <img src="https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/model-for-grouped-aggs.png?raw=true" alt="model-for-grouped-aggs.png" width="80%" height="80%">
# </center>

# ### Groups as index vs. variables
# 
# ```{note}
# Notice that the grouped variable becomes the Index in our example!
# ```

# In[23]:


ames.groupby('Neighborhood').agg({'SalePrice': ['mean', 'median']}).index


# This is the default behavior of pandas, and probably how pandas wants to be used.  In fact, this is the fastest way to do it, but it's a matter of less than a millisecond. However, you aren't always going to see people group by the index. Instead of setting the group as the index, we can set the group as a variable.
# 
# ```{tip}
# The grouped variable can remain a Series/variable by adding the `as_index = False` parameter/argument to `groupby()`.
# ```

# In[24]:


ames.groupby('Neighborhood', as_index=False).agg({'SalePrice': ['mean', 'median']}).head()


# ### Grouping by multiple variables
# 
# Sometimes we have multiple categories by which we'd like to group. To extend our example, assume we want to find the average sale price by neighborhood ***AND*** year sold. We can pass a list of variable names to the `groupby()` method:

# In[25]:


ames.groupby(['Neighborhood', 'Yr Sold'], as_index=False).agg({'SalePrice': 'mean'})


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. How would you convert the following statement into a grouped aggregation syntax: "what is the average above ground square footage of homes based on neighbhorhood and bedroom count"?
# 2. Compute the above statement (variable hints: `Gr Liv Area` = above ground square footage, `Neighborhood` = neighborhood, `Bedroom AbvGr` = bedroom count).
# 3. Using the results from #2, find out which neighborhoods have 1 bedrooms homes that average more than 1500 above ground square feet.
# ```

# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# Using the Ames housing data...
# 1. What neighbhorhood has the largest median sales price? (hint: check out `sort_values()`)
# 2. What is the mean and median sales price based on the number of bedrooms (`Bedroom AbvGr`)?
# 3. Which neighbhorhood has the largest median sales price for 3 bedroom homes? Which neighborhood has the smallest median sales price for 3 bedroom homes?
# 4. Compute the sales price per square footage (`Gr Liv Area`) per home. Call this variable `price_per_sqft`. Now compute the median `price_per_sqft` per neighborhood. Which neighborhood has the largest median `price_per_sqft`? Does this differ from the neighborhood identified in #1? What information does this provide you?
# ```

# ## Computing environment

# In[26]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab,pandas')

