#!/usr/bin/env python
# coding: utf-8

# # Lession 6a: Conditional statements
# 
# Conditional statements are a key part of any programming language.  Their purpose is to evaluate if some condition holds and then execute a particular task depending on the result.  The most common conditional statements are `if`, `elif`, and `else` statements. In this lesson we'll cover each of these along with a few additional applications of conditional statements.

# ```{admonition} Video 🎥:
# Get introduced to conditional statements with this intro video and then read the lesson that follows to learn more and to get some hands-on practice.
# 
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_adhkstgw&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[forceMobileHTML5]=true&amp;flashvars[scrubber.sliderPreview]=false&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_4xky5q5i" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043 | Python Tutorial for Beginners 6: Conditionals and Booleans - If, Else, and Elif Statements"></iframe>
# ```

# ## Learning objectives
# 
# By the end of this lesson you will be able to:
# 
# 1. Apply basic `if` statements along with additional multi-branching statements (i.e. `if...elif...else`).
# 2. Create Pythonic versions of switch statements.
# 3. Apply vectorized conditional statements on Pandas DataFrames.

# ## Prerequisites
# 
# Most of the examples in this lesson use base Python code without any modules; however, we will illustrate some examples of integrating control statements within Pandas. We also illustrate a couple examples that use Numpy.

# In[1]:


import pandas as pd
import numpy as np


# Also, most of the examples use toy data; however, when illustrating concepts integrated with Pandas we will use the  Complete Journey transaction data:

# In[2]:


from completejourney_py import get_data

df = get_data()['transactions']


# ## if statement
# 
# The conditional `if` statement is used to test an expression. If the `test_expression` is `True`, the statement gets executed. But if it’s `False`, nothing happens.
# 
# ```python
# if test_expression:
#     statement
# ```
# 
# The following is an example that tests if a particular object is negative. Notice that there are no braces or "begin/end" delimiters around the block of code. Python uses the indentation to determine blocks of code. Consequently, you can include multiple lines in the if statement as long as they have the same indentation.

# In[3]:


x = -8

if x < 0:
    print('x contains a negative number')


# In[4]:


# multiple lines in the statement are fine as long as they have the 
# same indentation
if x < 0:
    new_value = abs(x)
    print(f'absolute value of x is {new_value}')


# It is possible to write very short `if` statements on one line. This can be useful in limited situations but as soon as your resulting statement become more verbose it is best practice to switch to a multi-line approach.

# In[5]:


# single line approach
if x < 0: print('x contains a negative number')


# Its helpful to remember that everything in Python has some form of truthiness. In fact, any nonzero number or nonempty object is `True`. This allows you to evaluate the object directly:

# In[6]:


# a conditional statement on an empty object is equivalent to False
empty_list = []
if empty_list:
    print("since empty_list is False this won't exectute")


# In[7]:


# a conditional statement on a non-empty object is equivalent to True
non_empty_list = ['not', 'empty']
if non_empty_list:
    print("This list is not empty")


# Python uses `and` and `or` operators to evaluate multiple expressions. They always return a single `True` or `False`. Moreover, Python will stop evaluating multiple expressions as soon as the result is known.

# In[8]:


x = -1
y = 4
if x < 0 or y < 0:
    print('At least one of these objects are less than zero.')


# In[9]:


if x < 0 and y < 0:
    print('Both x and y or less than zero')


# ### Knowledge check
# 
# ```{admonition} Tasks:
# :class: attention
# Fill in the following code chunk so that:
# 
# * If month has value 1-9 the file name printed out will be "data/Month-0X.csv"
# * What happens if the month value is 10-12?
# 
#     ```python
#     month = 4
# 
#     if month ________ :
#         print(f'data/Month-0{month}.csv')
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_g2b8t7a0&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_96f0ntjn" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: if Statement Knowledge Check"></iframe>
# ```

# ## Multiway branching
# 
# Multiway branching is when we want to have multiple return statement options based on the input conditions. The general form of multiway branch `if` statements is as follows.
# 
# ```{note}
# The `elif` block is not necessary. If you want only two output branches then just use `if` followed by `else`. However, if you have many branches, you can use as many `elif` statements as necessary.
# ```
# ```python
# if test_1:
#   statement_1
# elif test2:
#   statement_2
# else:
#   statement_3
# ```
# 
# The following illustrates with a simple example. Python will perform this code in sequence and execute the statements nested under the first test that is `True` or the `else` if all tests are `False`.

# In[10]:


x = 22.50

if 0 <= x < 10:
    print('low')
elif 10 <= x < 20:
    print('medium-low')
elif 20 <= x < 30:
    print('medium')
else:
    print('preferred')


# ### Knowledge check
# 
# ```{admonition} Tasks:
# :class: attention
# Fill in the following code chunk so that:
# 
# * if month has value 1-9 the file name printed out will be "data/month-0X.csv"
# * if month has value 10-12 the file name printed out will be "data/month-1X.csv"
# * if month is an invalid month number (not 1-12), the result printed out is "Invalid month"
# * test it out for when month equals 6, 10, & 13
# 
#     ```python
#     month = 4
# 
#     if month ________:
#         print(f'data/Month-0{month}.csv')
#     _____:
#         print(f'data/Month-{month}.csv')
#     _____:
#         print('________')
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_ty18uk5l&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_xdcnvp3a" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Multi-way Branching Knowledge Check"></iframe>
# ```

# ## Switch statements
# 
# Many other languages have a `switch` or `case` statement that allows you to evaluate an expression and return the statement that aligns with the value. For example, in R, the `switch` statement looks like the following:
# 
# ```r
# choice <- 'ham'
# 
# switch(choice,
#        'spam'  = 1.25,
#        'ham'   = 1.99,
#        'eggs'  = 0.99,
#        'bacon' = 1.10,
# )
# ## [1] 1.99
# ```
# 
# Python does not have `switch` statement but has some handy alternatives. In the most basic approach, you could just use a multiway branch `if` statement:

# In[11]:


choice = 'ham'

if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')


# However, this approach is a bit verbose. An efficient alternative is to use a dictionary that provides the same key-value matching as a `switch` statement. 

# In[12]:


options = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}


# You can either index this dictionary for the matching key:

# In[13]:


options[choice]


# Or, a more trustworthy approach is to use the `get()` method. This allows you to provide a default response in the case that the key you are looking for is not in the dictionary
# 
# ```{tip}
# Using the `get()` method allows you to supply a value to provide if there is no matching key (or as in `if` statements if there are no other conditions that equate to `True`).
# ```

# In[14]:


options.get(choice, 'Bad choice')


# In[15]:


choice = 'broccoli'
options.get(choice, 'Bad choice')


# Dictionaries are good for associating values with keys, but what about the more complicated actions you can code in the statement blocks associated with `if` statements? Fortunately, dictionaries can also hold functions (both named functions and lambda functions) which can allow you to perform more sophisticated switch-like execution.
# 
# ```{note}
# Don't worry, you will learn more about functions in an upcoming lesson.
# ```

# In[16]:


def produce_revenue(sqft, visits, trend):
    total = 9.91 * sqft * visits * trend
    return round(total, 2)
  
def frozen_revenue(sqft, visits, trend):
    prod = produce_revenue(sqft, visits, trend)
    total = 3.28 * sqft * visits * trend - prod * .005 
    return round(total, 2)
  
expected_annual_revenue = {
    'produce':    produce_revenue, 
    'frozen':     frozen_revenue, 
    'pharmacy':   lambda: 16.11 * visits * trend
    }
  
choice = 'frozen'
expected_annual_revenue.get(choice, 'Bad choice')(sqft=937, visits=465, trend=0.98)


# ### Knowledge check
# 
# ```{admonition} Tasks:
# :class: attention
# Convert the following multi-branch `if-else` statement into a `dict` where you get the month path file with `path_files.get(month)`. In this case, which approach seems more reasonable?
# 
#     ```python
#     month = 4
# 
#     if month <= 9:
#         print(f'data/Month-0{month}.csv')
#     elif month >= 10 and month <= 12:
#         print(f'data/Month-{month}.csv')
#     else:
#         print('Invalid month')
# 
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_36iavgtw&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_yf6f6umd" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Switch Statement Knowledge Check"></iframe>
# ```

# ## Applying in Pandas
# 
# When data mining, we often want to perform conditional statements to not only filter observations, but also to create new variables. For example, say we want to create a new variable that classifies transactions above $10 as “high value” otherwise they are “low value”. There are several methods we can use to perform this but a simple one is to use the `apply` method:

# In[17]:


df['value'] = df['sales_value'].apply(lambda x: 'high value' if x > 10 else 'low value')
df.head()


# In[18]:


df.groupby('value').size()


# An alternative, and much faster approach is to use `np.where()`, which requires numpy to be loaded. `np.where` has been show to be over 2.5 times faster than `apply()`:

# In[19]:


df['value'] = np.where(df['sales_value'] > 10, 'high value', 'low value')
df.head()


# As our conditions get more complex, it often becomes useful to create a separate function and use `apply`.  This approach is probably the most legible; however, see [this post]() for a much faster approach if you are working with significantly large data.

# In[20]:


def flag(df):
    if (df['quantity'] > 20) or (df['sales_value'] > 10):
        return 'Large purchase'
    elif (df['quantity'] > 10) or (df['sales_value'] > 5):
        return 'Medium purchase'
    elif (df['quantity'] > 0) or (df['sales_value'] > 0):
        return 'Small purchase'
    else:
        return 'Alternative transaction'

df['purchase_flag'] = df.apply(flag, axis = 1)
df.head()


# In[21]:


df.groupby('purchase_flag').size()


# ```{admonition} Video 🎥:
# Here is a more thorough introduction to the `apply` method; plus, you'll also be introduced to the `map` and `applymap` methods.
# 
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_en445syw&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[forceMobileHTML5]=true&amp;flashvars[scrubber.sliderPreview]=false&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_9veqin0h" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043 | How do I apply a function to a pandas Series or DataFrame?"></iframe>
# ```

# ### Knowledge check
# 
# ```{admonition} Tasks:
# :class: attention
# Fill in the blanks below to assign each transaction to a power rating of 1, 2, 3, or 4 based on the `sales_value` variable:
# 
#    - power_rating = 1: if `sales_value` < 25th percentile
#    - power_rating = 2: if `sales_value` < 50th percentile
#    - power_rating = 3: if `sales_value` < 75th percentile
#    - power_rating = 4: if `sales_value` >= 75th percentile
# 
# **Hint:** use the `.quantile(perc_value)`
# 
#    ```python
#    low = df['sales_value'].quantile(____)
#    med = df['sales_value'].quantile(____) 
#    hig = df['sales_value'].quantile(____)
# 
#    def power_rater(df):
#       if (df['sales_value'] < _____):
#          return ___
#       elif (df['sales_value'] < _____):
#          return ___
#       elif (df['sales_value'] < _____):
#          return ___
#       else:
#          return ___
# 
#    df['power_rating'] = df.apply(power_rater, axis = 1)
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_p5ysnap2&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_k0uu9fxc" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Apply Statement Knowledge Check"></iframe>
# ```

# ## Exercises
# 
# ```{admonition} Tasks:
# :class: attention
# Using the Complete Journey `transactions` data:
# 
# 1. Create a new column titled `total_disc` that is the sum of all discounts applied to each transaction.
# 2. Create a new column `disc_rating` that classifies each transaction as:
#    - 'none': if `total_disc` == 0
#    - 'low': if `total_disc` < 25th percentile
#    - 'medium': if `total_disc` < 75th percentile
#    - 'high': if `total_disc` >= 75th percentile
#    - 'other': for any transaction that doesn't meet any of the above conditions
# 3. How many transactions are in each of the above `disc_rating` categories?
# ```

# ## Computing environment

# In[22]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p pandas,jupyterlab,completejourney_py')

