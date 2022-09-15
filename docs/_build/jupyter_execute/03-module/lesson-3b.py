#!/usr/bin/env python
# coding: utf-8

# # Lesson 3b: Manipulating data
# 
# > During the course of doing data analysis and modeling, a significant amount of time is spent on data preparation: loading, cleaning, transforming, and rearranging. Such tasks are often reported to take up 80% or more of an analyst's time.
# >
# > \- Wes McKinney, the creator of Pandas, in his book *Python for Data Analysis*
# 
# We've learned how to subset our DataFrames, in this lesson we'll focus on how to manipulate, create, drop, even identify missing value patterns across our DataFrame's columns.

# ## Learning objectives
# 
# By the end of this lesson you will be able to:
# 
# - Rename columns
# - Perform calculations and operations with one or more columns
# - Add, drop, and overwrite columns in your DataFrame
# - Identify missing values and replace these (and even non-missing) values.

# ## Renaming columns
# 
# Often, one of the first things we want to do with a new data set is clean up the column names. We can do this a few different ways and to illustrate, let's look at the Ames housing data:

# In[1]:


import pandas as pd

ames = pd.read_csv('../data/ames_raw.csv')
ames.head()


# Say we want to rename the "MS SubClass" and "MS Zoning" columns. We can do so with the `rename` method and passing a dictionary that maps old names to new names: `df.rename(columns={'old_name1': 'new_name1', 'old_name2': 'new_name2'})`.

# In[2]:


ames.rename(columns={'MS SubClass': 'ms_subclass', 'MS Zoning': 'ms_zoning'})
ames.head()


# Wait? What happened? Nothing changed? In the code above we did actually rename columns of our DataFrame but we didn’t modify the DataFrame inplace, we made a copy of it. There are generally two options for making permanent DataFrame changes:
# 
# 1. Use the argument `inplace=True`, e.g., `df.rename(..., inplace=True)`, available in most Pandas functions/methods
# 2. Re-assign, e.g., `df = df.rename(...)` The Pandas team recommends **Method 2 (re-assign)**, for a [few reasons](https://www.youtube.com/watch?v=hK6o_TDXXN8&t=700) (mostly to do with how memory is allocated under the hood).
# 
# ```{warning}
# Be sure to include the `columns=` when providing the argument dictionary. `rename` can be used to rename index values as well, which is actually the default behavior. So if you don't specify `columns=` it'll behave differently then expected and no error/warning messages will be provided.
# ```

# In[3]:


ames = ames.rename(columns={'MS SubClass': 'ms_subclass', 'MS Zoning': 'ms_zoning'})
ames.head()


# Using `rename` is great for renaming a single or even a handful of columns but can be tedious for renaming _many_ columns. For this we can use the `.columns` attribute, which just returns all the column names. 

# In[4]:


ames.columns


#  Pandas offers a lot of string methods that we can apply to string objects.
# 
# ```{tip}
# Check out some of the more common string methods [here](https://pandas.pydata.org/docs/user_guide/text.html#string-methods).
# ```
# 
# We can manipulate these column name values by using string methods that you can access via `.str.xxxx()`. For example, we can coerce all the column names to lower case with:

# In[5]:


ames.columns.str.lower()


# We can even chain multiple string methods together. For example the following coerces the column names to lower case, replaces all white space in the column names with an underscore, and then assigns these converted values back to the `.columns` attribute.

# In[6]:


ames.columns = ames.columns.str.lower().str.replace(" ", "_")
ames.head()


# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_5aaotn14&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_39dn7b1x" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Renaming Columns"></iframe>
# ```

# ## Calculations using columns

# It's common to want to modify a column of a DataFrame, or sometimes even to create a new column. For example, let's look at the `saleprice` column in our data.

# In[7]:


sale_price = ames['saleprice']
sale_price


# Say we wanted to convert the sales price of our homes to be represented as thousands; so rather than "215000" we want to represent it as "215"? To do this we can simply divide by 1,000.

# In[8]:


sale_price_k = sale_price / 1000
sale_price_k


# ## Adding & removing columns
# 
# So we've create a new series, `sale_price_k`. Right now it's totally separate from our original `ames` DataFrame, but we can make it a column of `ames` using the assignment syntax with the column reference syntax.
# ```python
# df['new_column_name'] = new_column_series
# ```

# In[9]:


ames['sale_price_k'] = sale_price_k
ames.head()


# Note that `ames` now has a "sale_price_k" column at the end.
# 
# ```{note}
# Also note that in the code above, the column name goes in quotes within the bracket syntax, while the values that will become the column -- the Series we're using -- are on the right side of the statement, without any brackets or quotes.
# ```
# 
# This sequence of operations can be expressed as a single line:

# In[10]:


ames['sale_price_k'] = ames['saleprice'] / 1000


# From a mathematical perspective, what we're doing here is adding a *scalar* -- a single value -- to a *vector* -- a series of values (aka a `Series`).
# Other vector-scalar math is supported as well.

# In[11]:


# Subtraction
(ames['saleprice']- 12).head()


# In[12]:


# Multiplication
(ames['saleprice'] * 10).head()


# In[13]:


# Exponentiation
(ames['saleprice'] ** 2).head()


# We may want to drop columns as well. For this we can use the `.drop()` method:

# In[14]:


ames = ames.drop(columns=['order', 'sale_price_k'])
ames.head()


# ### Knowledge check
# 
# ```{admonition} Question:
# :class: attention
# 1. Create a new column `utility_space` that is 1/5 of the above ground living space (`gr_liv_area`). 
# 2. You will get fractional output with step #1. See if you can figure out how to round this output to the nearest integer.
# 3. Now remove this column from your DataFrame
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_iqqb9wtg&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_ijxv54su" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Adding and Removing Columns"></iframe>
# ```

# ## Overwriting columns
# 

# What if we discovered a systematic error in our data? Perhaps we find out that the "lot_area" column is not entirely accurate because the recording process includes an extra 50 square feet for every property. We could create a new column, "real_lot_area" but we're not going to need the original "lot_area" column, and leaving it could cause confusion for others looking at our data.
# 
# A better solution would be to replace the original column with the new, recalculated, values. We can do so using the same syntax as for creating a new column.

# In[15]:


ames.head()


# In[16]:


# Subtract 50 from lot area, and then overwrite the original data.
ames['lot_area'] = ames['lot_area'] - 50


# In[17]:


ames.head()


# ## Calculating based on multiple columns

# So far we've only seen vector-scalar math. But vector-vector math is supported as well. Let's look at a toy example of creating a column that contains the price per square foot.

# In[18]:


price_per_sqft = ames['saleprice'] / ames['gr_liv_area']
price_per_sqft.head()


# In[19]:


ames['price_per_sqft'] = price_per_sqft
ames.head()


# You can combine vector-vector and vector-scalar calculations in arbitrarily complex ways.

# In[20]:


ames['nonsense'] = (ames['yr_sold'] + 12) * ames['gr_liv_area'] + ames['lot_area'] - 50
ames.head()


# ### Knowledge check
# 
# ```{admonition} Question:
# :class: attention
# Create a new column `price_per_total_sqft` that is `saleprice` divided by the sum of `gr_liv_area`, `total_bsmt_sf`, `wood_deck_sf`, `open_porch_sf`.
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_z7jvae57&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_8178wjna" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Calculations with Multiple Columns"></iframe>
# ```

# ## Non-numeric column operations

# For simplicity, we started with mathematical operations. However, pandas supports string operations as well. We can use `+` to concatenate strings, with both vectors and scalars.

# In[21]:


'Home in ' + ames['neighborhood'] + ' neighborhood sold under ' + ames['sale_condition'] + ' condition'


# More complex string operations are possible using methods available through the `.str` *accessor*.
# 
# 
# ```{tip}
# We won't cover them in detail, so refer to the [documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html) if you're interested. But realize that we can do _many_ different manipulations with string columns and its worth taking time to familiarize yourself with Pandas string capabilities.
# ```

# In[22]:


# number of characters in string
ames['neighborhood'].str.len()


# In[23]:


ames['garage_type'].str.lower().str.replace('tchd', 'tached')


# ## More Complex Column Manipulation

# ### Replacing Values
# 
# One fairly common situation in data wrangling is needing to convert one set of values to another, where there is a one-to-one correspondence between the values currently in the column and the new values that should replace them.
# This operation can be described as "mapping one set of values to another".
# 
# Let's look at an example of this. In our Ames data the month sold is represented numerically:

# In[24]:


ames['mo_sold'].head()


# Suppose we want to change this so that values are represented by the month name:
# 
# - 1 = 'Jan'
# - 2 = 'Feb'
# - ...
# - 12 = 'Dec'
# 
# We can express this *mapping* of old values to new values using a Python dictionary.

# In[25]:


# Only specify the values we want to replace; don't include the ones that should stay the same.
value_mapping = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
    }


# Pandas provides a handy method on Series, `.replace`, that accepts this value mapping and updates the Series accordingly.
# We can use it to recode our values.

# In[26]:


ames['mo_sold'].replace(value_mapping).head()


# If you are a SQL user, this workflow may look familiar to you;
# it's quite similar to a `CASE WHEN` statement in SQL.

# ### Missing values
# 
# Missing values are typically denoted with NaN. We can use `df.isnull()` to find missing values in a dataframe. It returns a boolean for each element in the dataframe:

# In[27]:


ames.isnull()


# We can use this to easily compute the total number of missing values in each column:

# In[28]:


ames.isnull().sum()


# Recall we also get this information with `.info()`. Actually, we get the inverse as `.info()` tells us how many non-null values exist in each column.

# In[29]:


ames.info()


# We can use `any()` to identify which columns have missing values. We can use this information for various reasons such as subsetting for just those columns that have missing values.

# In[30]:


missing = ames.isnull().any() # identify if missing values exist in each column
ames[missing[missing].index]  # subset for just those columns that have missing values


# When you have missing values, we usually either drop them or impute them.You can drop missing values with `.dropna()`:

# In[31]:


ames.dropna()


# Whoa! What just happened? Well, this data set actually has a missing value in every single row. `.dropna()` drops every row that contains a missing value so we end up dropping _all_ observations.  Consequently, we probably want to figure out what's going on with these missing values and isolate the column causing the problem and imputing the values if possible.
# 
# ```{tip}
# Another "drop" method is `.drop_duplcates()` which will drop duplicated rows in your DataFrame.
# ```
# 

# Sometimes visualizations help identify patterns in missing values. One thing I often do is print a heatmap of my dataframe to get a feel for where my missing values are. We'll get into data visualization in future lessons but for now here is an example using the **searborn** library. We can see that several variables have a lot of missing values (`alley`, `fireplace_qu`, `pool_qc`, `fence`, `misc_feature`).

# In[32]:


import seaborn as sns
sns.set(rc={'figure.figsize':(12, 8)})


# In[33]:


ames_missing = ames[missing[missing].index]
sns.heatmap(ames_missing.isnull(), cmap='viridis', cbar=False);


# Since we can't drop all missing values in this data set (since it leaves us with no rows), we need to impute ("fill") them in. There are several approaches we can use to do this; one of which uses the `.fillna()` method. This method has various options for filling, you can use a fixed value, the mean of the column, the previous non-nan value, etc:

# In[34]:


import numpy as np

# example DataFrame with missing values
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list('ABCD'))
df


# In[35]:


df.fillna(0)  # fill with 0


# In[36]:


df.fillna(df.mean())  # fill with the mean


# In[37]:


df.fillna(method='bfill')  # backward (upwards) fill from non-nan values


# In[38]:


df.fillna(method='ffill')  # forward (downward) fill from non-nan values


# ### Applying custom functions
# 
# There will be times when you want to apply a function that is not built-in to Pandas. For this, we have methods:
# 
# * `df.apply()`, applies a function column-wise or row-wise across a dataframe (the function must be able to accept/return an array)
# * `df.applymap()`, applies a function element-wise (for functions that accept/return single values at a time)
# * `series.apply()`/`series.map()`, same as above but for Pandas series
# 
# For example, say you had the following custom function that defines if a home is considered a luxery home simply based on the price sold.
# 
# ```{note}
# Don't worry, you'll learn more about writing your own functions in future lessons!
# ```

# In[39]:


def is_luxery_home(x):
    if x > 500000:
        return 'Luxery'
    else:
        return 'Non-luxery'

ames['saleprice'].apply(is_luxery_home)


# This may have been better as a lambda function, which is just a shorter approach to writing functions. This may be a bit confusing but we'll talk more about lambda functions in the writing functions lesson. For now, just think of it as being able to write a function for single use application on the fly.

# In[40]:


ames['saleprice'].apply(lambda x: 'Luxery' if x > 500000 else 'Non-luxery')


# You can even use functions that require additional arguments. Just specify the arguments in `.apply()`:

# In[41]:


def is_luxery_home(x, price):
    if x > price:
        return 'Luxery'
    else:
        return 'Non-luxery'

ames['saleprice'].apply(is_luxery_home, price=200000)


# Sometimes we may have a function that we want to apply to every element across multiple columns. For example, say we wanted to convert several of the square footage variables to be represented as square meters. For this we can use the [`.applymap()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.applymap.html) method.

# In[42]:


def convert_to_sq_meters(x):
    return x*0.092903

ames[['gr_liv_area', 'garage_area', 'lot_area']].applymap(convert_to_sq_meters)


# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# 1. Import the heart.csv dataset.
# 2. Are there any missing values in this data? If so, which columns? For these columns, fill the missing values with the value that appears most often (aka "mode"). This is a multi-step process and it would be worth reviewing the [`.fillna()` docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html).
# 3. Create a new column called `risk` that is equal to $ \frac{age}{\text{res_bp} + chol + \text{max_hr}} $
# 4. Replace the values in the `rest_ecg` column so that:
#    - normal = normal
#    - left ventricular hypertrophy = lvh
#    - ST-T wave abnormality = stt_wav_abn
# ```

# ## Computing environment

# In[43]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab,pandas,numpy,seaborn')

