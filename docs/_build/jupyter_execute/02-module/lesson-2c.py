#!/usr/bin/env python
# coding: utf-8

# # Lesson 2c: Deeper dive on DataFrames
# 
# Now that we know how to import data as a DataFrame, let's spend a little time discussing DataFrames and what they are made up of. This should create a stronger foundation of Pandas and DataFrames.
# 
# ## Learning objectives
# 
# At the end of this lesson you should be able to:
# 
# * Explain the difference between DataFrames and Series
# * Set and manipulate index values
# 
# To illustrate our points throughout this lesson, we'll use the following airlines data which simply includes the name of the airline carrier and the airline carrier code:

# In[1]:


import pandas as pd

df = pd.read_csv('../data/airlines.csv')
df.head()


# ## What Are DataFrames Made of?
# 
# Accessing an individual column of a DataFrame can be done by passing the column name as a string, in brackets (`[]`).

# In[2]:


carrier_column = df['carrier']
carrier_column


# Individual columns are pandas `Series` objects.

# In[3]:


type(carrier_column)


# A Series is like a NumPy array but with labels. They are strictly 1-dimensional and can contain any data type (integers, strings, floats, objects, etc), including a mix of them. Series can be created from a scalar, a list, ndarray or dictionary using `pd.Series()` (note the captial “S”). Here are some example series:
# 
# <center>
# <img src="https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/series-illustration.png?raw=true" alt="import-framework.png" width="80%" height="80%"/>
# </center>
# 
# How are Series different from DataFrames?
# 
# - They're always 1-dimensional
# - They have different attributes & methods than DataFrames
#     - For example, Series have a `to_list` method -- which doesn't make sense to have on DataFrames
# - They don't print in the pretty format of DataFrames, but in plain text (see above)

# In[4]:


# A Series only has one dimension (number of elements)
carrier_column.shape


# In[5]:


# Whereas a DataFrame has two (rows and columns)
df.shape


# As mentioned above, Series will have different attributes & methods than DataFrames. For example, Series have a `to_list` method which converts the single array of values into a list. This is a common practice in a lot of workflows. However, a DataFrame does not have this method.

# In[6]:


# A unique method to Series
carrier_column.to_list()


# In[7]:


# DataFrames don't have this method so we'll get an error!
df.to_list()


# It's important to be familiar with Series because they are fundamentally the core of DataFrames.
# 
# <center>
# <img src="https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/dataframe-illustration.png?raw=true" alt="import-framework.png" width="80%" height="80%"/>
# </center>
# 
# Not only are columns represented as Series, but so are rows!

# In[39]:


df.head(1)


# In[29]:


# Fetch the first row of the DataFrame
first_row = df.loc[0]
first_row


# In[26]:


type(first_row)


# ```{note}
# Whenever you select individual columns or rows, you'll get Series objects.
# ```

# ## What Can You Do with a Series?

# First, let's create our own Series object from scratch -- they don't need to come from a DataFrame. Here, we pass a list in as an argument and it will be converted to a Series.

# In[40]:


s = pd.Series([10, 20, 30, 40, 50])
s


# There are 3 things to notice about this Series:
# 
# - The values (10, 20, 30...)
# - The *dtype*, short for data type.
# - The *index* (0, 1, 2...)
# 
# **Values** are fairly self-explanatory; we chose them in our input list. 
# 
# **Data types** are also straightforward. Series are often homogeneous, holding only integers, floats, or generic Python objects (called just `object`); however, they actually can hold a mix of data types (though this is quite rare and we'll stay away from doing this for the most part). As we mentioned in the last lesson, string elements in DataFrames are often labeled as having an _object_ dtype. Because a Python object is general enough to contain any other type, any Series holding strings or other non-numeric data will typically default to be of type `object`.

# For example, going back to our carriers DataFrame, note that the carrier column is of type `object`.

# In[27]:


df['carrier']


# **Indexes** are more interesting. Every Series has an index, a way to reference each element. The index of a Series is a lot like the keys of a dictionary: each index element corresponds to a value in the Series, and can be used to look up that element.

# In[42]:


# Our index is a range from 0 (inclusive) to 5 (exclusive).
s.index


# In[29]:


s


# As we learned to index other data structures in the previous module, we can continue to use `[]` for indexing Series. When we specify below, we are stating to get the 4th element in our Series located at index value 3.

# In[30]:


s[3]


# In our example, the index is just the integers 0-4, so right now it looks no different that referencing elements of a regular Python list.
# *But* indexes can be changed to something different -- like the letters a-e, for example.

# In[43]:


s.index = ['a', 'b', 'c', 'd', 'e']
s


# Now to look up the value 40, we reference `'d'`.

# In[32]:


s['d']


# We saw earlier that rows of a DataFrame are Series.
# In such cases, the flexibility of Series indexes comes in handy;
# the index is set to the DataFrame column names.

# In[33]:


df.head()


# In[34]:


# Note that the index is ['carrier', 'name']
first_row = df.loc[0]
first_row


# This is particularly handy because it means you can extract individual elements based on a column name.

# In[35]:


first_row['carrier']


# ## DataFrame Indexes
# 
# It's not just Series that have indexes! DataFrames have them too. Take a look at the carrier DataFrame again and note the bold numbers on the left.

# In[36]:


df.head()


# These numbers are an index, just like the one we saw on our example Series.
# And DataFrame indexes support similar functionality.

# In[37]:


# Our index is a range from 0 (inclusive) to 16 (exclusive).
df.index


# When loading in a DataFrame, the default index will always be 0 to N-1, where N is the number of rows in your DataFrame.
# This is called a `RangeIndex`. Selecting individual rows by their index is done with the `.loc` accessor.
# 
# ```{tip}
# An **accessor** is an attribute designed specifically to help users reference something else (like rows within a DataFrame).
# ```

# In[38]:


# Get the row at index 4 (the fifth row).
df.loc[4]


# As with Series, DataFrames support reassigning their index. However, with DataFrames it often makes sense to change one of your columns into the index. This is analogous to a primary key in relational databases: a way to rapidly look up rows within a table.
# 
# In our case, maybe we will often use the carrier code (`carrier`) to look up the full name of the airline. In that case, it would make sense set the carrier column as our index.

# In[45]:


df = df.set_index('carrier')
df.head()


# Now the RangeIndex has been replaced with a more meaningful index, and it's possible to look up rows of the table by passing carrier code to the `.loc` accessor.

# In[46]:


df.loc['AA']


# ```{warning}
# Pandas does not require that indexes have unique values (that is, no duplicates) although many relational databases do have that requirement of a primary key. This means that it is *possible* to create a non-unique index, but highly inadvisable. Having duplicate values in your index can cause unexpected results when you refer to rows by index -- but multiple rows have that index. Don't do it if you can help it!
# ```

# When starting to work with a DataFrame, it's often a good idea to determine what column makes sense as your index and to set it immediately. This will make your code nicer -- by letting you directly look up values with the index -- and also make your selections and filters faster, because Pandas is optimized for operations by index. If you want to change the index of your DataFrame later, you can always `reset_index` (and then assign a new one).

# In[47]:


df.head()


# In[48]:


df = df.reset_index()
df.head()


# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# Import the airports data as `airports`. The data contains the airport code, airport name, and some basic facts about the airport location.
# 
# 1. What kind of index is the current index of `airports`? 
# 2. Is this a good choice for the DataFrame's index? If not, what column or columns would be a better candidate?
# 3. Set the `faa` column as your new index.
# 4. Using your new index, look up "Pittsburgh-Monroeville Airport", which has FAA code 4G0. What is its altitude?
# 5. Reset your index in case you want to make a different column your index in the future.
# ```

# ## Computing environment

# In[3]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab,pandas')

