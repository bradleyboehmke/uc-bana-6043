#!/usr/bin/env python
# coding: utf-8

# # Lesson 4b: Relational data
# 
# It’s rare that a data analysis involves only a single table of data. Typically you have many tables of data, and you must combine them to answer the questions that you’re interested in. Collectively, multiple tables of data are called **relational data** because its the relations, not just the individual data sets, that are important. 
# 
# To work with relational data you need join operations that work with pairs of tables. There are several types of join methods to work with relational data and in this lesson we are going to explore these various methods.

# ## Learning objectives
# 
# By the end of this lesson you'll be able to:
# 
# * Use various mutating joins to combine variables from two tables.
# * Join two tables that have differing common key variable names.
# * Include an indicator variable while joining so you can filter the joined data for follow-on analysis.
# 
# ```{admonition} Video 🎥:
# Here's a great video discussing ways to join DataFrames. Watch this video for an initial introduction and then get more hands on by working through the lesson that follows.
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/iYWKfUOtGaw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ```

# ## Prerequisites
# 
# Load Pandas to provide you access to the join functions we’ll cover in this lesson.

# In[1]:


import pandas as pd


# To illustrate various joining tasks we will use two very simple DataFrames `x` & `y`. The colored column represents the “key” variable: these are used to match the rows between the tables. We'll talk more about keys in a second. The grey column represents the “value” column that is carried along for the ride. 
# 
# :::{figure-md} simple-dataframes
# <img src="../images/original-dfs.png" alt="Example DataFrames" width="50%">
# 
# Two simple DataFrames.
# :::

# In[2]:


x = pd.DataFrame({'id': [1, 2, 3], 'val_x': ['x1', 'x2', 'x3']})
y = pd.DataFrame({'id': [1, 2, 4], 'val_y': ['y1', 'y2', 'y4']})


# However, we will also build upon the simple examples by using various data sets from the **completejourney_py** library. This library provides access to data sets characterizing household level transactions over one year from a group of 2,469 households who are frequent shoppers at a grocery store.
# 
# There are eight built-in data sets available in this library. The data sets include:
# 
# - **campaigns**: campaigns received by each household
# - **campaign_descriptions**: campaign metadata (length of time active)
# - **coupons**: coupon metadata (UPC code, campaign, etc.)
# - **coupon_redemptions**: coupon redemptions (household, day, UPC code, campaign)
# - **demographics**: household demographic data (age, income, family size, etc.)
# - **products**: product metadata (brand, description, etc.)
# 
# This is a Python equivalent of the R package [completejourney](https://github.com/bradleyboehmke/completejourney). The R package has a full guide to get you acquainted with the various data set schemas, which you can read [here](https://bradleyboehmke.github.io/completejourney/articles/completejourney.html).

# In[3]:


from completejourney_py import get_data

# get_data() provides a dictionary of several DataFrames
cj_data = get_data()
cj_data.keys()


# In[4]:


cj_data['transactions'].head()


# ```{admonition} TODO
# :class: attention
# Take some time to read about the completejourney data set schema [here](https://bradleyboehmke.github.io/completejourney/articles/completejourney.html#dataset-details).  
# 
# 1. What different data sets are available and what do they represent?
# 2. What are the common variables between each table?
# ```

# ## Keys
# 
# The variables used to connect two tables are called **keys**. A key is a variable (or set of variables) that uniquely identifies an observation. There are two primary types of keys we'll consider in this lesson:
# 
# * A __primary key__ uniquely identifies an observation in its own table
# * A __foreign key__ uniquely identifies an observation in another table
# 
# Variables can be both a primary key and a foreign key. For example, within the transactions data `household_id` is a primary key to represent a household identifier for each transaction. `household_id` is also a foreign key in the demographics data set where it can be used to align household demographics to each transaction.
# 
# A primary key and the corresponding foreign key in another table form a relation. Relations are typically one-to-many. For example, each transaction has one household, but each household has many transactions. In other data, you’ll occasionally see a 1-to-1 relationship.
# 
# When data is cleaned appropriately the keys used to match two tables will be commonly named. For example, the variable that can link our `x` and `y` data sets is named `id`:

# In[5]:


x.columns.intersection(y.columns)


# We can easily see this by looking at the `x` and `y` data but when working with larger data sets this becomes more appropriate than just viewing the data. For example, we can easily identify the common columns in the completejourney_py transactions and demographics data:

# In[6]:


transactions = cj_data['transactions']
demographics = cj_data['demographics']

transactions.columns.intersection(demographics.columns)


# ```{note}
# Although it is preferred, keys do not need to have the same name in both tables. For example, our household identifier could be named `household_id` in the transaction data but be `hshd_id` in the demographics table. The names would be different but they represent the same information.
# ```

# ## Mutating joins
# 
# Often we have separate DataFrames that can have common and differing variables for similar observations and we wish to join these DataFrames together. A mutating join allows you to combine variables from two tables. It first matches observations by their keys, then copies across variables from one table to the other.
# 
# There are different types of joins depending on how you want to merge two DataFrames:
# 
# - **inner join**: keeps only observations in `x` that match in `y`.
# - **left join**: keeps all observations in `x` and adds available information from `y`.
# - **right join**: keeps all observations in `y` and adds available information from `x`.
# - **full join**: keeps all observations in both `x` and `y`.
# 
# Let's explore each of these a little more closely.
# 
# ```{note}
# DataFrames have two different methods to join data - `df.join()` & `df.merge()`. The `.join` method is meant for joining based on the index rather than columns. In practice, `.merge` tends to be used more often because it allows us to retain variables in columns and join by one or more columns. Consequently, we will be using `.merge` throughout this lesson.
# ```

# ### Inner join
# 
# The simplest type of join is the **inner join**. An inner join matches pairs of observations whenever their keys are equal. Consequently, the output of an inner join is all rows from `x` where there are matching values in `y`, and all columns from `x` and `y`.
# 
# ```{note}
# An inner join is the most restrictive of the joins - it returns only rows with matches across both data frames.
# ```
# 
# The following provides a nice illustration:
# 
# :::{figure-md} inner-join
# <img src="../images/join-inner.png" alt="Inner join"  width="50%">
# 
# Inner join ([source](https://r4ds.had.co.nz/relational-data.html)).
# :::

# To perform an inner join with Pandas we use the `.merge` method. By default, `.merge` will perform an inner join:

# In[7]:


x.merge(y)


# ```{note}
# Notice that only those rows where there are common key values (`id` = 1 & 2) in both `x` and `y` are retained while the rows where non-common key values exist (`id` = 3 in `x` and `id` = 4 in `y`) are discarded.
# ```
# 
# Note that I didn’t specify which column to join on nor the type of join. If that information is not specified, merge uses the overlapping column names as the keys. It’s a good practice to specify the type of join and the keys explicitly:

# In[8]:


x.merge(y, how='inner', on='id')


# ### Outer joins
# 
# An inner join keeps observations that appear in both tables. However, we often want to retain *all* observations in at least one of the tables. Consequently, we can apply various **outer joins** to retain observations that appear in at least one of the tables. There are three main types of outer joins:
# 
# * A left join keeps all observations in `x`.
# * A right join keeps all observations in `y`.
# * A full join keeps all observations in `x` and `y`.
# 
# These joins work by adding `NaN` in rows where non-matching information exists:
# 
# :::{figure-md} outer-join
# <img src="../images/join-outer.png" alt="Outer joins"  width="50%">
# 
# Difference in left join, right join, and outer join procedures ([source](https://r4ds.had.co.nz/relational-data.html)).
# :::
# 
# 

# #### Left join
# 
# With a **left join** we retain all observations from `x`, and we add columns `y`. Rows in `x` where there is no matching key value in `y` will have `NaN` values in the new columns. We can change the type of join by changing the `how` argument.

# In[9]:


x.merge(y, how='left', on='id')


# #### Right join
# 
# A **right join** is just a flipped left join where we retain all observations from `y`, and we add columns `x`. Similar to a left join, rows in `y` where there is no matching key value in `x` will have `NaN` values in the new columns.
# 
# ```{note}
# Should I use a right join, or a left join? To answer this, ask yourself _“which DataFrame should retain all of its rows?”_ - and use this one as the baseline. A left join keeps all the rows in the first DataFrame written in the command, whereas a right join keeps all the rows in the second DataFrame.
# ```

# In[10]:


x.merge(y, how='right', on='id')


# #### Full outer join
# 
# We can also perform a **full outer join** where we keep all observations in `x` and `y`. This join will match observations where the key variable(s) have matching information in both tables and then fill in non-matching values as `NaN`.
# 
# ```{note}
# A full outer join is the most inclusive of the joins - it returns all rows from both DataFrames.
# ```

# In[11]:


x.merge(y, how='outer', on='id')


# ## Differing keys
# 
# So far, the keys we've used to join two DataFrames have had the same name. This was encoded by using `on='id'`. However, having keys with the same name is not a requirement. But what happens we our common key variable is named differently in each DataFrame?

# In[12]:


a = pd.DataFrame({'id_a': [1, 2, 3], 'val_a': ['x1', 'x2', 'x3']})
b = pd.DataFrame({'id_b': [1, 2, 4], 'val_b': ['y1', 'y2', 'y4']})


# In this case, since our common key variable has different names in each table (`id_a` in `a` and `id_b` in `b`), our inner join function doesn't know how to join these two DataFrames and an error results. 

# In[13]:


a.merge(b)


# When this happens, we can explicitly tell our join function to use unique key names in each DataFrame as a common key with the `left_on` and `right_on` arguments:

# In[34]:


a.merge(b, left_on='id_a', right_on='id_b')


# ## Bigger example
# 
# So far we've used small simple examples to illustrate the differences between joins. Now let's use our **completejourney** data to look at some larger examples.  
# 
# Say we wanted to add product information (via `products`) to each transaction (`transaction`); however, we want to *retain all transactions*. This would suggest a left join so we can keep all transaction observations but simply add product information where possible to each transaction.
# 
# First, let's get the common key:

# In[41]:


products = cj_data['products']

# common variables
transactions.columns.intersection(products.columns)


# This aligns to the [data dictionary](https://bradleyboehmke.github.io/completejourney/articles/completejourney.html#dataset-details) so we can trust this is the accurate common key. We can now perform a left join using `product_id` as the common key.
# 
# ```{tip}
# The join functions add variables to the right, so if you have a lot of variables already you will need to scroll over to the far right to see the newly added variables.
# ```

# In[42]:


transactions.merge(products, how='left', on='product_id')


# This has now added product information to each transaction. Consequently, if we wanted to get the total sales across the meat `department` but summarized at the `product_category` level so that we can identify which products generate the greatest sales we could follow this joining procedure with additional skills we learned in previous lessons:

# In[46]:


(
    transactions
    .merge(products, how='left', on='product_id')
    .query("department == 'MEAT'")
    .groupby('product_category', as_index=False)
    .agg({'sales_value': sum})
    .sort_values(by='sales_value', ascending=False)
)


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. Join the `transactions` and `demographics` data so that you have household demographics for each transaction. Now compute the total sales by `age` category to identify which age group generates the most sales.
# 2. Use successive joins to join `transactions` with `coupons` and then with `coupon_redemptions`. Use the proper join that will only retain those transactions that have coupon and coupon redemption data.
# ```

# ## Merge indicator
# 
# You can use the `indicator` argument to add a special column `_merge` that indicates the source of each row; values will be `left_only`, `right_only`, or `both` based on the origin of the joined data in each row.

# In[36]:


x.merge(y, how='outer', indicator=True)


# This can be used for additional filtering or other informational reasons. For example, say our manager came to us and asked -- _"of all our transactions, how many of them are by customers that we **don't** have demographic information on?"_ To answer this question we could use an indicator and then just find those transactions that are in `_merge = left_only` since those are transactions that don't have matching demographic information.
# 
# We see that of the 1,469,307 transactions...

# In[40]:


# Total number of transactions
transactions.shape


# 640,457 (43%) of them are by customers that we don't have demographic info on.

# In[39]:


# Number of transactions with no customer demographic information
(
    transactions
    .merge(demographics, how='outer', indicator=True)
    .query("_merge == 'left_only'")
).shape


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. Using the `products` and `transactions` data, how many products have and have not sold? In other words, of all the products we have in our inventory, how many have been involved in a transaction? How many have not been involved in a transaction?
# 2. Using the `demographics` and `transactions` data, identify which `income` level buys the most `quantity` of goods.
# ```

# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# 1. Get demographic information for all households that have total sales (`sales_value`) of $100 or more.
# 2. Of the households that have total sales of $100 or more, how many of these customers do we not have demographic information on?
# 3. Using the `promotions` and `transactions` data, compute the total sales for all products that were in a display in the front of the store (`display_location` --> 1).
# ```

# ## Computing environment

# In[49]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab,pandas,completejourney_py')

