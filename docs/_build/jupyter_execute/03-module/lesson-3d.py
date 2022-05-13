#!/usr/bin/env python
# coding: utf-8

# # Summarizing Grouped Data

# ## Applied Review

# ### DataFrame Structure

# * We will start by importing the `planes` data set as a DataFrame:

# In[1]:


import pandas as pd
planes_df = pd.read_csv('../data/planes.csv')


# * Each DataFrame variable is a **Series** and can be accessed with bracket subsetting notation: 
# 
# ```python 
# DataFrame['SeriesName']
# ```

# * The DataFrame has an **Index** that is visible the far left side

# ### Summary Operations

# * Summary operations occur when we collapse a Series or DataFrame down to a single row

# * This is an aggregation of a variable across its rows

# <center>
# <img src="images/aggregate-series.png" alt="aggregate-series.png" width="400" height="400">
# </center>

# ### Summarizing Data Frames

# * We can perform summary operations on DataFrames in a number of ways:
#   * Summary methods for a specific summary operation: 
#   ```python 
#   DataFrame.sum()
#   ```
#   * Describe method for a collection of summary operations: 
#   ```python
#   DataFrame.describe()
#   ```
#   * Agg method for flexibility in summary operations: 
#   ```python
#   DataFrame.agg({'VariableName': ['sum', 'mean']})
#   ```

# * An example of the agg method:

# In[2]:


planes_df.agg({
    'year': ['mean', 'median'],
    'seats': ['mean', 'max']
})


# <div class="admonition note alert alert-info">
#     <b><p class="first admonition-title" style="font-weight: bold">Note</p></b>
#     <p>We will primarily use the <tt class=\"docutils literal\">.agg()</tt> method moving forward.</p>
# </div>

# ## General Model

# ### Variable Groups

# * We can group DataFrame rows together by the value in a Series/variable
# * If we "group by A", then rows with the same value in variable A are in the same group

# <img src="images/dataframe-groups.png" width="50%" height="50%"/>

# * Note that groups do not need to be ordered by their values:

# <img src="images/dataframe-groups-unordered.png" width="50%" height="50%"/>

# <div class="admonition tip alert alert-warning">
#     <b><p class="first admonition-title" style="font-weight: bold">Question</p></b>
#     <p>Why might we be interested in grouping by a variable?</p>
# </div>

# ### Summarizing by Groups

# * When we've talked about **summary** operations, we've talked about collapsing a DataFrame to a single row

# * This is not always the case -- we sometimes collapse to a *single row per group*

# * This is known as a grouped aggregation:

# ![summarizing-by-groups.png](images/summarizing-by-groups.png)

# * This can be useful when we want to aggregate by cateogory:
#   * Maximum temperature *by month*
#   * Total home runs *by team*
#   * Total sales *by geography*
#   * Average number of seats by plane manufacturer

# <div class="admonition tip alert alert-warning">
#     <b><p class="first admonition-title" style="font-weight: bold">Question</p></b>
#     <p>What are common grouped aggregation metrics used in your industry/organization?</p>
# </div>

# ## Summarizing Grouped Data

# * When we summarize by groups, we can use the same aggregation methods we previously did
#   * Summary methods for a specific summary operation: 
#   ```python
#   DataFrame.sum()
#   ```
#   * Describe method for a collection of summary operations: 
#   ```python
#   DataFrame.describe()
#   ```
#   * Agg method for flexibility in summary operations: 
#   ```python
#   DataFrame.agg({'VariableName': ['sum', 'mean']})
#   ```

# * The only difference is the need to **set the DataFrame group prior to aggregating**

# ### Setting the DataFrame Group

# * We can set the DataFrame group by calling the `DataFrame.groupby()` method and passing a variable name:

# In[3]:


planes_df.groupby('model')


# * Notice that a DataFrame doesn't print when it's grouped

# * The `groupby()` method is just setting the group - you can see the changed DataFrame class:

# In[4]:


type(planes_df.groupby('manufacturer'))


# * If we then call an aggregation method, we will see the DataFrame returned with the aggregated results:

# In[5]:


planes_df.groupby('manufacturer').agg({'seats': ['mean', 'max']}).head()


# * This process always follows this model:
# 
# ![model-for-grouped-aggs.png](images/model-for-grouped-aggs.png)

# * **Notice that the grouped variable becomes the Index in our example!**

# In[6]:


planes_df.groupby('manufacturer').agg({'seats': ['mean', 'max']}).head()


# In[7]:


planes_df.groupby('manufacturer').agg({'seats': ['mean', 'max']}).index


# #### Groups as Indexes

# * This is the default behavior of `pandas`, and probably how `pandas` wants to be used

# * This is the fastest way to do it, but it's a matter of less than a millisecond

# * You aren't always going to see people group by the Index...

# #### Groups as Variables

# * Instead of setting the group as the Index, we can set the group as a variable

# * The grouped variable can remain a Series/variable by adding the `as_index = False` parameter/argument to `groupby()`:

# In[8]:


planes_df.groupby('manufacturer', as_index = False).agg({'seats': ['mean', 'max']}).head()


# ### Grouping by Multiple Variables

# * Sometimes we have multiple categories by which we'd like to group

# * To extend our example, assume we want to find the average number of seats by plane manufacturer AND plane year

# * We can pass a list of variable names to the `groupby()` method:

# In[9]:


planes_df.groupby(['manufacturer', 'year'], as_index = False).agg({'seats': ['mean', 'max']}).head()


# <font class="your_turn">
#     Your Turn
# </font>
# 
# 1\. What is meant by "find the minimum number of seats on a plane by year"?
# 
# 2\. Fix the below code to find the minimum number of seats on a plane by year:
# 
#    ```python
#    planes_df.groupby('_____').agg({'_____': ['min']})
#    ```
#    
# 3\. What is the Index of the result?

# ## Questions
# 
# Are there any questions before we move on?
