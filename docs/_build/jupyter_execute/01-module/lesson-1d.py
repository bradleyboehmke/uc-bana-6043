#!/usr/bin/env python
# coding: utf-8

# # Lesson 1d: Data structures
# 
# <hr/>

# So far we've worked with single values: numbers, strings, and booleans. But Python also supports more complex data types, sometimes called ***data structures***.
# 
# There are three very common built-in data structures that we are going to learn about in this lesson: **lists**, **tuples**, and **dictionaries**.
# 
# ## Learning objectives
# 
# By the end of this lesson you will be able to:
# 
# * Explain the difference between lists, tuples, and dictionaries and when to use each.
# * Create and manage these data structures along with how to apply operators on them.

# ## Lists
# 
# Lists and tuples allow us to store multiple things (“elements”) in a single object. The elements are considered ordered, which just means the elements remain in the same position as when created unless they are manually re-ordered. Let's start with lists. 
# 
# ### Creation
# 
# Lists are represented using brackets (`[]`).

# In[1]:


# A list of integers
numbers = [1, 2, 3]
numbers


# In[2]:


type(numbers)


# In[3]:


# A list of strings
strings = ['abc', 'def']
strings


# Lists are highly flexible. They can contain heterogeneous data (i.e. strings, booleans, and numbers can all be in the same list) and lists can even contain other lists!

# In[4]:


# Lists containing heterogeneous data
combo = ['a', 'b', 3, 4]
combo_2 = [True, 'True', 1, 1.0]

# Note that the last element of the list is another list!
nested_list = [1, 2, 3, [4, 5]]
nested_list


# We can also create a list by type conversion with `list()`. For example, we can convert a string into a list of characters.

# In[5]:


my_str = 'A string.'
list(my_str)


# ### Indexing
# 
# Individual elements of a list can be accessed by specifying a location in brackets. This is called **indexing**. So, say we want to get the first item from a list:
# 

# In[6]:


letters = ['a', 'b', 'c']
letters[1]


# Wait a minute! Shouldn’t letters[1] give the first item in the list? It seems to give the second. This is because indexing in Python starts at zero. 
# 
# ```{warning}
# Python uses zero-based indexing, so the first element is element 0! (Historical note: [Why Python uses zero-based indexing](http://python-history.blogspot.com/2013/10/why-python-uses-0-based-indexing.html).)

# In[7]:


letters[0]


# In[8]:


letters[2]


# Specifying an invalid location will raise an error.

# In[9]:


letters[4]


# ```{note}
# Most programming languages are zero indexed, so a list with 3 elements has valid locations [0, 1, 2]. But this means that there is no element #3 in a 3-element list! Trying to access it will cause an out-of-range error. This is a common mistake for those new to programming (and sometimes it bites the veterans too).
# ```

# ### Slicing
# 
# Now, what if we want to pull out multiple _sequential_ items in a list? We call this **slicing**? We can use colons (`:`) for that.

# In[10]:


letters_in_my_name = list('brad boehmke')

# first 3 elements
letters_in_my_name[0:3]


# We got elements 0 through 2 even though we stated `0:3`. When using the colon indexing, `my_list[i:j]`, we get items `i` through `j-1`.
# 
# ```{note}
# The slice range is inclusive of the first index and exclusive of the last. If the slice’s final index is larger than the length of the sequence, the slice ends at the last element.
# ```
# 
# We can even get away with not specifying the first or last number if we wish to get all elements up to, or all elements starting with, a certain element.

# In[11]:


# all elements up to element 3
letters_in_my_name[0:3]


# In[12]:


# all elements starting with element 3
letters_in_my_name[2:]


# One last thing to note is that we can specify a **stride**. The stride comes after a second colon. For example, if we only wanted to get every other element

# In[13]:


# stride of 2 will get every other element
letters_in_my_name[::2]


# So, in general, the indexing scheme is:
# 
# `my_list[start:end:stride]`
# 
# * If there are no colons, a single element is returned.
# * If there are any colons, we are slicing the list, and a list is returned.
# * If there is one colon, `stride` is assumed to be 1.
# * If `start` is not specified, it is assumed to be zero.
# * If `end` is not specified, the interpreted assumed you want the entire list.
# * If `stride` is not specified, it is assumed to be 1.
# 
# ```{note}
# There are a lot of options here and I don't expect you to remember them after first glance. Just realize that slicing is extremely flexible!
# ```

# ### Operators
# 
# Operators on lists behave much like operators on strings. The `+` operator on lists means list concatenation.

# In[14]:


[1, 2, 3] + [4, 5, 6]


# The `*` operator on lists means list replication and concatenation.

# In[15]:


[1, 2, 3] * 3


# Membership operators are used to determine if an item is in a list. The two membership operators are:
# 
# | English | Operator |
# | ------- | -------- |
# | is a member of | `in` |
# | is not a member of | `not in` |

# The result of the operator is `True` or `False`. Let’s look at letters again:

# In[16]:


'a' in letters


# In[17]:


'z' in letters


# ```{note}
# Membership operators are case sensitive!
# ```

# In[18]:


'A' not in letters


# These membership operators offer a great convenience for conditionals.

# In[19]:


first_inital = 'b'

if first_inital in letters:
    print('My first initial is in the list!')
else:
    print('Aw shucks!')


# 
# ### Mutability
# 
# Lists are **mutable**. This means we can change their values without creating a new list. (You cannot change the data type or identity.) Let’s see this by example.

# In[20]:


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list[3] = 'four'

my_list


# The other data types we have encountered so far, `int`egers, `float`s, and `str`ings, are immutable. You cannot change their values without reassigning them. To see this, we’ll use the `id()` function, which tells us where in memory that the variable is stored. (Note: this identity is unique to the Python interpreter, and should not be considered an actual physical address in memory.)

# In[21]:


a = 8451
print(id(a))

a = 8452
print(id(a))


# So, we see that the identity of `a`, an integer, changed when we tried to change its value. So, we didn’t actually change its value; we made a new variable. With lists, though, this is not the case.

# In[22]:


print(id(my_list))

my_list[0] = 'zero'
print(id(my_list))


# ```{tip}
# It is still the same list! This is very important to consider when we do assignments.
# ```

# ### Knowledge check
# 
# ```{admonition} Questions
# :class: attention
# Given the following list `l = [10, [3, 4], [5, [100, 200, ["BANA"]], 23, 11], 1, 7]`
# 
# 1. Use indexing to grab the word “BANA”.
# 2. Change the value of "BANA" to "BANA 6043".
# 3. Use slicing to get the last 4 elements.
# ```

# ## Tuples
# 
# A **tuple** is just like a list, except it is immutable (basically a read-only list). 
# 
# ```{note}
# What I just said there is explosive, as described in this [blog post](http://www.asmeurer.com/blog/posts/tuples/). Tuples do have many other capabilities beyond what you would expect from just being “a read-only list,” but for us just beginning now, we can think of it that way.
# ```
# 
# ### Creation
# 
# A tuple is created just like a list, except we use parentheses `()` instead of brackets. The only watch-out is that a tuple with a single item needs to include a comma after the item.

# In[23]:


my_tuple = ('a', 'b', 'c')
type(my_tuple)


# In[24]:


a_tuple = (0,)   # Create a single element tuple
not_a_tuple = (0) # This is just the number 0 (normal use of parantheses)

type(a_tuple), type(not_a_tuple)


# We can also create a tuple by doing a type conversion. We can convert our list to a tuple.

# In[25]:


name_as_string = 'brad boehmke'
name_as_list = list(name_as_string)
name_as_tuple = tuple(name_as_list)

name_as_tuple


# ### Indexing & slicing
# 
# Similar to lists, we can index and slice using `[]` notation and specifying the elements of interest. The only difference is when slicing, we get a tuple in return rather than a list.

# In[26]:


# Last letter
name_as_tuple[-1]


# In[27]:


name_as_tuple[0:3]


# ### Operators
# 
# 
# As with lists we can concatenate tuples with the `+` operator.

# In[28]:


(1, 2, 3) + (4, )


# Membership operators work the same as with lists.

# In[29]:


'z' in name_as_tuple


# 
# 
# ### Mutability
# 
# As we stated at the beginning of this section, tuples are immutable. This means once we've created a tuple we can not change the existing elements inside it.

# In[30]:


name_as_tuple[0] = 'B'


# ### Tuple unpacking
# 
# Tuples allow for a special assignment process. We call this _tuple unpacking_ and it allows us to assign individual items from a tuple to their own variable.
# 
# ```{note}
# This is useful when we want to return more than one value from a function and further using the values as stored in different variables. We will make use of this later in this class.
# ```

# In[31]:


my_name = ('Brad', 'Boehmke')
first, last = my_name


# In[32]:


first


# In[33]:


last


# ### Knowledge check
# 
# ```{admonition} Questions
# :class: attention
# Given the following tuple `schooling = ('UC', 'BANA', '6043')`
# 
# 1. Use indexing to grab the word “BANA”.
# 2. Change the value of "BANA" to "Business Analytics". What happens?
# 3. Unpack the `schooling` tuple into three variables: `university`, `program`, `class`.
# ```

# ## Dictionaries
# 
# Dictionaries are collections of _key-value pairs_. Think of a real dictionary -- you look up a word (a key), to find its definition (a value). Any given key can have only one value.
# 
# This concept has many names depending on language: map, associative array, dictionary, and more.
# 
# ### Creation
# 
# In Python, dictionaries are represented with curly braces `{}`. Colons separate a key from its value, and (like lists and tuples) commas delimit elements.

# In[34]:


brad = {'first_name': 'Brad',
        'last_name': 'Boehmke',
        'alma_mater': 'NDSU',
        'employer': '84.51˚',
        'zip_code': 45385}
brad


# Dictionaries, like lists, are very flexible. Keys are generally strings (though some other types are allowed), and values can be anything -- including lists or other dictionaries!

# In[35]:


ethan = {
    'first_name': 'Ethan',
    'last_name': 'Swan',
    'alma_mater': 'Notre Dame',
    'employer': '84.51˚',
    'zip_code': 45208
    }

# A dictionary of dictionaries!
instructors = {'brad': brad, 'ethan': ethan}
instructors


# ### Indexing
# 
# Similar to lists and tuples, we can index using brackets. However, rather than indexing with an element number we index by passing the key in the brackets (`my_dict['key']`).

# In[36]:


brad['employer']


# You’ll get a `KeyError` if you try to access a non-existent key:

# In[37]:


brad['undergrad']


# Although not necessarily indexing, we can also use the `keys()` and `values()` methods to extract the keys-values information.
# 
# ```{note}
# Don't worry about the what type of object these outputs are, just realize that we can extract them in this manner.
# ```

# In[38]:


brad.keys()


# In[39]:


brad.values()


# ### Operators
# 
# Dictionaries do not support concatenation operators like lists and tuples...

# In[40]:


brad + {'number': '800-867-5309'} # not my number so don't actually call it!


# But they do support membership operators; however, keep in mind that membership operators are focusing on the `key`s, not the values.

# In[41]:


'zip_code' in brad


# ### Mutability
# 
# Dictionaries are mutable. This means that they can be changed in place. For example, if we want to add an element to a dictionary, we use simple syntax.

# In[42]:


brad['first_name'] = 'Bradley'   # Change an existing value
brad['number'] = '800-867-5309'  # Add a new key-value pair
brad


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# Imagine you need a way to quickly determine a company's CEO given the company name. You could use a dictionary such that ceos['company_name'] = 'CEO name'. 
# 1. Create a dictionary `ceos` with two company CEOs:
#    - Apple: Tim Cook
#    - Microsoft: Satya Nadella
# 2. Now add Bob Iger as the CEO of Disney.
# 3. Now you realize that Bob Iger is no longer the CEO of Disney; rather, it is Bob Chapek. Update the Disney CEO to reflect this change.
# ```

# ## Quick Review
# 
# | English name | Type | Type category | Description | Example |
# | ------------ | ---- | ------------- | ----------- | ------- |
# | list         | `list` | Sequence type | a collection of objects - mutable & ordered | `['Brad', 2022, ['another', 'list']]` |
# | tuple        | `tuple` | Sequence type | a collection of objects - immutable & ordered | `('Brad', 2022, ['embedded', 'list'])` |
# | dictionary   | `dict` | Mapping type | mapping of key-value pairs - mutable & ordered | `{'name': 'BANA', 'code': 6043, 'credits': 2}` |

# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# Imagine you need a way to quickly determine a company's CEO given the company name. You could use a dictionary such that ceos['company_name'] = 'CEO name'. 
# 1. Create a string that contains your name. Convert this string to a list. Check if the letter 'p' is in this list.
# 2. Why does the following cell return an error?
#    ```python
#    t = (1, 2, 3, 4, 5)
#    t[-1] = 6
#    
# 3. Given this nest dictionary grab the word “BANA”
#    ```python
#    d = {
#        "a_list": [1, 2, 3,],
#         "a_dict": {"first": ["this", "is", "inception"], 
#                    "second": [1, 2, 3, "BANA"]}
#    }
#     
# ```

# ## Computing environment

# In[43]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab,pandas')

