#!/usr/bin/env python
# coding: utf-8

# # Manipulating and Creating Columns

# > During the course of doing data analysis and modeling, a significant amount of time is spent on data preparation: loading, cleaning, transforming, and rearranging. Such tasks are often reported to take up 80% or more of an analyst's time.
# >
# > \- Wes McKinney, the creator of Pandas, in his book *Python for Data Analysis*

# ## Applied Review

# ### Data Structures and DataFrames
# - We use **DataFrames** to represent tables in Python.
# - Python also supports other data structures for storing information that isn't tabular. Examples include lists and dictionaries.
# - DataFrames have many **methods**, or functions that access their internal data. Some examples we saw were `describe()` and `set_index()`.
# - DataFrames are composed of **Series**, 1-D data structures (like a vector). DataFrame columns can be thought of as Series.

# ### Importing Data
# - Python can read in data from CSVs, JSON files, and pickle files with just a few lines of code.

# ### Selecting and Filtering Data
# - Python's pandas library supports limiting rows (via *filtering* and *slicing*), as well as *selecting* columns.
# - All of these operations use the bracket operators, but row syntax includes the `.loc` *accessor*.

# ## Calculations Using Columns

# It's common to want to modify a column of a DataFrame, or sometimes even to create a new column.
# Let's take a look at our planes data again.

# In[1]:


import pandas as pd

planes = pd.read_csv('../data/planes.csv')
planes.head()


# Suppose we wanted to know the total capacity of each plane, including the crew.
# We have data on how many seats each plane has (in the `seats` column), but that only includes paying passengers.
# 
# 

# In[2]:


seats = planes['seats']
seats.head()


# For simplicity, let's say a full flight crew is always 5 people.
# Series objects allow us to perform addition with the regular `+` syntax –- in this case, `seats + 5`.

# In[3]:


capacity = seats + 5
capacity.head()


# <div class="admonition tip alert alert-warning">
#     <b><p class="first admonition-title" style="font-weight: bold">Question</p></b>
#     <p>What happens if you switch the order? (i.e. <tt class=\"docutils literal\">5 + seats</tt>)? Does this make sense?</p>
# </div>

# So we've create a new series, `capacity`, with the total capacity of the plane.
# Right now it's totally separate from our original `planes` DataFrame, but we can make it a column of `planes` using the assignment syntax with the column reference syntax.
# ```python
# df['new_column_name'] = new_column_series
# ```

# In[4]:


planes['capacity'] = capacity
planes.head()


# Note that `planes` now has a "capacity" column at the end.

# <div class="admonition note alert alert-info">
#     <b><p class="first admonition-title" style="font-weight: bold">Note</p></b>
#     <p>Also note that in the code above, the <b><i>column name</i></b> goes in quotes within the bracket syntax, while the <b><i>values that will become the column</i></b> -- the Series we're using -- are on the right side of the statement, without any brackets or quotes.</p>
# </div>

# This sequence of operations can be expressed as a single line:

# In[5]:


# Create a capacity column filled with the values in the seats column added with 5.
planes['capacity'] = planes['seats'] + 5


# From a mathematical perspective, what we're doing here is adding a *scalar* -- a single value -- to a *vector* -- a series of values (aka a `Series`).
# Other vector-scalar math is supported as well.

# In[6]:


# Subtraction
(planes['seats'] - 12).head()


# In[7]:


# Multiplication
(planes['seats'] * 10).head()


# In[8]:


# Exponentiation
(planes['seats'] ** 2).head()


# <font class="your_turn">
#     Your Turn
# </font>
# 
# Create a new column named "first_class_seats" that is 1/5 of the total seats on the plane. You will have some results with fractional seats; don't worry about this.

# ## Overwriting Columns
# 

# What if we discovered a systematic error in our data?
# Perhaps we find out that the "engines" column is only the number of engines *per wing* -- so the total number of engines is actually double the value in that column.

# We could create a new column, "real_engine_count" or "total_engines".
# But we're not going to need the original "engines" column, and leaving it could cause confusion for others looking at our data.

# A better solution would be to replace the original column with the new, recalculated, values.
# We can do so using the same syntax as for creating a new column.

# In[9]:


planes.head()


# In[10]:


# Multiply the engines column by 2, and then overwrite the original data.
planes['engines'] = planes['engines'] * 2


# In[11]:


planes.head()


# ## Calculating Values Based on Multiple Columns

# So far we've only seen vector-scalar math.
# But vector-vector math is supported as well.

# Let's look at a toy example of creating a column that contains the number of seats per engine.

# In[12]:


seats_per_engine = planes['seats'] / planes['engines']
seats_per_engine.head()


# In[13]:


planes['seats_per_engine'] = seats_per_engine
planes.head()


# You can combine vector-vector and vector-scalar calculations in arbitrarily complex ways.

# In[14]:


planes['nonsense'] = (planes['year'] + 12) * planes['engines'] + planes['seats'] - 9
planes.head()


# <font class="your_turn">
#     Your Turn
# </font>
# 
# Create a new column in the planes DataFrame, "technology_index", that is calculated with the formula:
# 
# `technology_index = (year-1900) / 4 + engines * 2`
# 
# Remember order of operations!

# In[15]:


planes['technology_index'] = (planes['year'] - 1900) / 4 + planes['engines'] * 2
planes


# ## Non-numeric Column Operations

# For simplicity, we started with mathematical operations.
# However, pandas supports string operations as well.

# We can use `+` to concatenate strings, with both vectors and scalars.

# In[16]:


summary = 'Tailnum is ' + planes['tailnum'] + ' and Model is ' + planes['model']
summary.head()


# More complex string operations are possible using methods available through the `.str` *accessor*.
# We won't cover them in detail, so refer to the [documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html) if you're interested.

# In[17]:


# Make the manufacturer field lowercase.
lowercase_mfctr = planes['manufacturer'].str.lower()
lowercase_mfctr.head()


# In[18]:


# Get the length of the tail number.
tailnum_len = planes['tailnum'].str.len()
tailnum_len.head()


# ## More Complex Column Manipulation

# ### Replacing Values

# One fairly common situation in data wrangling is needing to convert one set of values to another, where there is a one-to-one correspondence between the values currently in the column and the new values that should replace them.
# This operation can be described as "mapping one set of values to another".

# Let's look at an example of this.

# In[19]:


airlines = pd.read_csv('../data/airlines.csv')
# Keep just the first 5 rows for this example.
airlines = airlines.iloc[:5]
airlines


# Suppose we learn that there is a mistake in the carrier codes and they should be updated.
# - 9E should be PE
# - B6 should be BB
# - The other codes should stay as they are.

# We can express this *mapping* of old values to new values using a Python dictionary.

# In[20]:


# Only specify the values we want to replace; don't include the ones that should stay the same.
value_mapping = {'9E': 'PE',
                 'B6': 'BB'}


# Pandas provides a handy method on Series, `.replace`, that accepts this value mapping and updates the Series accordingly.
# We can use it to create a new column, "updated_carrier", with the proper carrier code values.

# In[21]:


airlines['updated_carrier'] = airlines['carrier'].replace(value_mapping)
airlines


# If you are a SQL user, this workflow may look familiar to you;
# it's quite similar to a `CASE WHEN` statement in SQL.

# <font class="your_turn">
#     Your Turn
# </font>
# 
# 1. Open the weather CSV (path: `../data/weather.csv`) and store it in a variable called `weather`.
# 2. Take a look at the "month" column. Observe that its values are numeric, not strings. How do you think these values relate to months of the year?
# 3. Create a mapping from each number to the corresponding month name, as a dictionary. For example, one of the keys would be `5` and its value would be `May`. Store it in a variable called `month_mapping`.
# 4. Use the `.replace` method to overwrite the current month column with the month names as strings, using your newly created mapping.

# ### The `apply` Method and Beyond

# If you can think of a way to express a new column as a combination of other columns and constants, it can be created using Python and Pandas.
# However, column calculations beyond the above are outside the scope of this training.

# If you wish to learn more, take a look at the [`DataFrame.apply` method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html).

# # Questions
# 
# Are there any questions before we move on?
