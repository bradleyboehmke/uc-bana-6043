#!/usr/bin/env python
# coding: utf-8

# # Lesson 6b: Iteration statement
# 
# Often, we need to execute repetitive code statements a particular number of times. Or, we may even need to execute code for an undetermined number of times until a certain condition no longer holds. There are multiple ways we can achieve this and in this lesson we will cover several of the more common approaches to perform iteration.

# ## Learning objectives
# 
# By the end of this lesson you will be able to:
# 
# * Apply `for` and `while` loops to execute repetitive code statements.
# * Incorporate `break` and `continue` to control looping statements.
# * Explain what a list comprehension is and implement variations of them.
# * Discuss the concept of iterables.

# ```{admonition} Video 🎥:
# First, check out this video for a simple introduction to `for` and `while` loops. Then move on to the lesson that follows which will reiterate and build upon these basic concepts.
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/6iF8Xb7Z3wQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ```

# ## Prerequisites

# In[1]:


import glob
import os
import random
import pandas as pd


# ## `for` loop
# 
# The `for` loop is used to execute repetitive code statements for a particular number of times. The general syntax is provided below where `i` is the counter and as `i` assumes each sequential value the code in the body will be performed for that ith value.
# 
# ```python
# # syntax of for loop
# for i in sequence:
#     <do stuff here with i>
# ```
# 
# There are three main components of a `for` loop to consider:
# 
# 1. __Sequence__: The sequence represents each element in a list or tuple, each key-value pair in a dictionary, or each column in a DataFrame.
# 2. __Body__: apply some function(s) to the object we are iterating over.
# 3. __Output__: You must specify what to do with the result.  This may include printing out a result or modifying the object in place.
# 
# For example, say we want to iterate N times, we can perform a for loop using the `range()` function:

# In[2]:


for number in range(10):
    print(number)


# We can add multiple lines to our `for` loop; we just need to ensure that each line follows the same indentation patter:

# In[3]:


for number in range(10):
    squared = number * number
    print(f'{number} squared = {squared}')


# Rather than just print out some result, we can also assign the computation to an object. For example, say we wanted to assign the squared result in the previous `for` loop to a dictionary where the key is the original number and the value is the squared value.

# In[4]:


squared_values = {}

for number in range(10):
    squared = number * number
    squared_values[number] = squared

squared_values


# ### Knowledge check
# 
# We can see all data sets that we have in the “data/monthly_data” folder with `glob.glob`:

# In[5]:


monthly_data_files = glob.glob("../data/monthly_data/*")
monthly_data_files


# If you wanted to get just the file name from the string path we can use `os.path.basename`:

# In[6]:


file_name = os.path.basename(monthly_data_files[0])
file_name


# And if we wanted to just get the name minus the file extension we can apply some simple string indexing to remove the last four characters (`.csv`):

# In[7]:


file_name[:-4]


# ```{admonition} Tasks:
# :class: attention
# Use this knowledge to:
# 
# 1. Create an empty dictionary called `monthly_data`.
# 2. Loop over `monthly_data_files` and assign the file name as the dictionary key and assign the file path as the value.
# 3. Loop over `monthly_data_files` and assign the file name as the dictionary key, import the data with `pd.read_csv()` and assign the imported DataFrame as the value in the dictionary.
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_8380bzml&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_ih2q3r2g" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: For Loop Knowledge Check"></iframe>
# ```

# ## Controlling sequences
# 
# There are two ways to control the progression of a loop:
# 
# * `continue`: terminates the current iteration and advances to the next.
# * `break`: exits the entire for loop.
# 
# Both are used in conjunction with if statements. For example, this for loop will iterate for each element in `year`; however, when it gets to the element that equals the year of `covid` (2020) it will `break` out and end the for loop process.

# In[8]:


# range will produce numbers starting at 2018 and up to but not include 2023
years = range(2018, 2023)
list(years)


# In[9]:


covid = 2020

for year in years:
    if year == covid: break
    print(year)


# The `continue` argument is useful when we want to skip the current iteration of a loop without terminating it. On encountering `continue`, the Python parser skips further evaluation and starts the next iteration of the loop. In this example, the for loop will iterate for each element in year; however, when it gets to the element that equals covid it will skip the rest of the code execution simply jump to the next iteration.

# In[10]:


for year in years:
    if year == covid: continue
    print(year)


# ### Knowledge check
# 
# ```{admonition} Tasks:
# :class: attention
# Modify the following for `loop` with a `continue` or `break` statement to:
# 
# 1. only import Month-01 through Month-07
# 2. only import Month-08 through Month-10
# 
# ```python
# monthly_data_files = glob.glob("../data/monthly_data/*")
# monthly_data = {}
# 
# for file in monthly_data_files:
#     file_name = os.path.basename(file)[:-4]
#     monthly_data[file_name] = pd.read_csv(file)
# 
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_76dej1zp&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_iwgdmxxq" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Sequence Control Knowledge Check"></iframe>
# ```

# ## List comprehensions
# 
# List comprehensions offer a shorthand syntax for `for` loops and are very common in the Python community. Although a little odd at first, the way to think of list comprehensions is as a backward `for` loop where we state the expression first, and then the sequence.  
# 
# ```python
# # syntax of for loop
# for i in sequence:
#     expression
#   
# # syntax for a list comprehension
# [expression for i in sequence]
# ```
# 
# Often, we'll see a pattern like the following where we:
# 
# 1. create an empty object (list in this example)
# 2. loop over an object and perform some computation
# 3. save the result to the empty object

# In[11]:


squared_values = []
for number in range(5):
    squared = number * number
    squared_values.append(squared)

squared_values


# A list comprehension allows us to condense this pattern to a single line:

# In[12]:


squared_values = [number * number for number in range(5)]
squared_values


# List comprehensions even allow us to add conditional statements. For example, here we use a conditional statement to skip even numbers:

# In[13]:


squared_odd_values = [number * number for number in range(10) if number % 2 != 0]
squared_odd_values


# For more complex conditional statements, or if the list comprehension gets a bit long, we can use multiple lines to make it easier to digest:

# In[14]:


squared_certain_values = [
    number * number for number in range(10) 
    if number % 2 != 0 and number != 5
    ]

squared_certain_values


# There are other forms of comprehensions as well. For example, we can perform a dictionary comprehension where we follow the same patter; however, we use dict brackets (`{`) instead of list brackets (`[`):

# In[15]:


squared_values_dict = {number: number*number for number in range(10)}
squared_values_dict


# ```{admonition} Video 🎥:
# Check out this video that provides more discussion and examples of using comprehensions.
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/3dt4OGnU5sM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ```

# ### Knowledge check
# 
# ```{admonition} Tasks:
# :class: attention
# Re-write the following `for` loop using a dictionary comprehension:
# 
# ```python
# monthly_data_files = glob.glob("../data/monthly_data/*")
# monthly_data = {}
# 
# for file in monthly_data_files:
#     file_name = os.path.basename(file)[:-4]
#     monthly_data[file_name] = pd.read_csv(file)
# 
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_ms8xup88&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_5o1nds4g" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Comprehensions Knowledge Check"></iframe>
# ```

# ## `while` loop
# 
# We may not always know how many iterations we need to make. Rather, we simply want to perform some task while a particular condition exists. This is the job of a `while` loop. A `while` loop follows the same logic as a `for` loop, except, rather than specify a sequence we want to specify a condition that will determine how many iterations.
# 
# ```python
# # syntax of for loop
# while condition_holds:
#     <do stuff here with i>
# ```
# 
# For example, the probability of flipping 10 coins and getting all heads or tails is $(\frac{1}{2})^{10} = 0.0009765625$ (1 in 1024 tries). Let's implement this and see how many times it'll take to accomplish this feat.
# 
# The following `while` statement will check if the number of unique values for 10 flips are 1, which implies that we flipped all heads or tails. If it is not equal to 1 then we repeat the process of flipping 10 coins and incrementing the number of tries. When our condition statement `ten_of_a_kind == True` then our while loop will stop.

# In[16]:


# create a coin
coin = ['heads', 'tails']

# we'll use this to track how many tries it takes to get 10 heads or 10 tails
n_tries = 0

# signals if we got 10 heads or 10 tails
ten_of_a_kind = False

while not ten_of_a_kind:
    # flip coin 10 times
    ten_coin_flips = [random.choice(coin) for flip in range(11)]
    
    # check if there
    ten_of_a_kind = len(set(ten_coin_flips)) == 1

    # add iteration to counter
    n_tries += 1


print(f'After {n_tries} flips: {ten_coin_flips}')


# ### Knowledge check
# 
# ```{admonition} Tasks:
# :class: attention
# An elementary example of a random walk is the random walk on the integer number line, $Z$, which starts at 0 and at each step moves +1 or −1 with equal probability.
# 
# Fill in the incomplete code chunk below to perform a random walk starting at value 0, with each step either adding or subtracting 1. Have your random walk stop if the value it exceeds 100 or if the number of steps taken exceeds 10,000.
# 
# ```python
# value = 0
# n_tries = 0
# exceeds_100 = False
# 
# while not exceeds_100 or _______:
#     # randomly add or subtract 1
#     random_value = random.choice([-1, 1])
#     value += _____
# 
#     # check if value exceeds 100
#     exceeds_100 = ______
# 
#     # add iteration to counter
#     n_tries += _____
# 
#   
# print(f'The final value was {value} after {n_tries} iterations.')
# 
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_0thymndn&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_73w498uh" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: while Loop Knowledge Check"></iframe>
# ```

# ## Iterables
# 
# Python strongly leverages the concept of _iterable objects_. An object is considered _iterable_ if it is either a physically stored sequence, or an object that produces one result at a time in the context of an interation tool like a `for` loop. Up to this point, our example looping structures have primarily iterated over a DataFrame or a list.
# 
# When our `for` loop iterates over a DataFrame, underneath the hood it is first accessing the iterable object, and then iterating over each item. As the following illustrates, the default iterable components of a DataFrame are the columns:

# In[17]:


df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [3, 4, 5], 'col3': [6, 6, 6]})

I = df.__iter__() # access iterable object
print(next(I))    # first iteration
print(next(I))    # second iteration
print(next(I))    # third iteration


# When our `for` loop iterates over a list, the same procedure unfolds. Note that when no more items are available to iterate over, a `StopIteration` is thrown which signals to our `for` loop that no more itertions should be performed. 

# In[18]:


names = ['Robert', 'Sandy', 'John', 'Patrick']

I = names.__iter__() # access iterable object
print(next(I))       # first iteration
print(next(I))       # second iteration
print(next(I))       # third iteration
print(next(I))       # fourth iteration
print(next(I))       # no more items


# Dictionaries and tuples are also iterable objects. Iterating over dictionary automatically returns one key at a time, which allows us to have the key and index for that key at the same time:

# In[68]:


D = {'a':1, 'b':2, 'c':3}

I = D.__iter__()  # access iterable object
print(next(I))    # first iteration
print(next(I))    # second iteration
print(next(I))    # third iteration


# In[69]:


for key in D:
    print(key, D[key])


# Although using these iterables in a for loop is quite common, you will often see two other approaches which include the iterables `range()` and `enumerate()`. range is often used to generate indexes in a for loop but you can use it anywhere you need a series of integers. However, range is an iterable that generates items on demand:

# In[70]:


values = range(5)

I = values.__iter__()
print(next(I))
print(next(I))
print(next(I))


# So if you wanted to iterate over each column in our DataFrame, an alternative is to use range. In this example, range produces the numeric index for each column so we simply use that value to index for the column within the for loop:

# In[72]:


unique_values = []
for col in range(len(df.columns)):
  value = df.iloc[:, col].nunique()
  unique_values.append(value)
  
unique_values


# Another common iterator you will see is `enumerate`. Actually, the `enumerate` function returns a **generator object**, which also supports this iterator concept. The benefit of `enumerate` is that it returns a (index, value) tuple each time through the loop:

# In[73]:


E = enumerate(df) # access iterable object
print(next(E))    # first iteration
print(next(E))    # second iteration
print(next(E))    # third iteration


# The `for` loop steps through these tuples automatically and allows us to unpack their values with tuple assignment in the header of the `for` loop. In the following example, we unpack the tuples into the variables `index` and `col` and we can now use both of these values however necessary in a for loop.

# In[74]:


for index, col in enumerate(df):
    print(f'{index} - {col}')


# ```{note}
# There are additional iterable objects that can be used in looping structures (i.e. zip, map); however, the ones discussed here are the most common you will come across and likely use.
# ```
# 
# ```{admonition} Video 🎥:
# Learn more about iterables and a similar, yet different concept -- _'iterators'_ with this video.
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/jTYiNjvnHZY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ```

# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# 1. For the following list of names, write a list comprehension that creates a list of only words that start with a capital letter (hint: `str.isupper()`). Which names are included in the result?
#    
#     ```python
#     names = ['Steve Irwin', 'koala', 'kangaroo', 'Australia', 'Sydney', 'desert']
# 
# 2. The Fibonacci Sequence is a series of numbers where the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34. Use a `for` loop to produce the first 25 numbers in the Fibanacci Sequence (0, 1, 1, 2, 3, 5, 8, 13, 21...)
# 
# 3. Create a `for` loop that sums the numbers from 0 through 100; however, skip the numbers in the following list:
# 
#     ```python
#     skip_these_numbers = [8, 29, 43, 68, 98]
# 
# ```

# ## Computing environment

# In[1]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p pandas,jupyterlab')

