#!/usr/bin/env python
# coding: utf-8

# # Lesson 6C: Writing functions
# 
# Functions are an essential part of any scripting language and as a data scientist, you’ll constantly need to write your own functions to solve problems that your data poses to you. Writing functions allows you to reduce your code, minimize errors, and make it more explicit in the actions being taken.  This lesson will get you started writing your own functions to improve your data analyses.

# ## Learning objectives
# 
# By the end of this lesson you will be able to:
# 
# * Explain when to write functions
# * Discuss the difference between functions and methods
# * Define your own functions that includes:
#    - Default arguments
#    - Type hints
#    - Exception handling
#    - Docstrings
# * Discuss how Python scopes for variables to use in functions
# * Apply `lambda` (anonymous) functions

# ```{admonition} Video 🎥:
# First, check out this video for a simple introduction to writing functions. Then move on to the lesson that follows which will reiterate and build upon these basic concepts.
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/9Os0o3wzS_I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ```

# ## Prerequisites

# In[1]:


import numpy as np
import pandas as pd
from completejourney_py import get_data

df = get_data()['transactions']


# ## When to write functions
# 
# You should consider writing a function whenever you’ve copied and pasted a block of code more than twice (i.e. you now have three copies of the same code). For example, take a look at this code. What does it do?

# In[2]:


# array containing 4 sets of 10 random numbers
x = np.random.random_sample((4, 10))
          
x[0] = (x[0] - x[0].min()) / (x[0].max() - x[0].min())
x[1] = (x[1] - x[1].min()) / (x[1].max() - x[1].min())
x[2] = (x[2] - x[2].min()) / (x[1].max() - x[2].min())
x[3] = (x[3] - x[3].min()) / (x[3].max() - x[3].min())


# You might be able to puzzle out that this rescales each array to have a range from 0 to 1. But did you spot the mistake? I made an error when copying-and-pasting the code for the third array: I forgot to change an `x[1]` to an `x[2]`. Writing a function reduces the chance of this error and makes it more explicit regarding our intentions since we can name our action (`rescale`) that we want to perform:

# In[3]:


x = np.random.random_sample((4, 10))

def rescale(array):
    for index, vector in enumerate(array):
        array[index] = (vector - vector.min()) / (vector.max() - vector.min())
    
    return(array)

rescale(x)


# ## Functions vs methods
# 
# Functions and methods are very similar, and beginners to object oriented programming languages such as Python often refer to them synonymously. Although they are very similar, it is always good to distinguish between the two as it will help you explain code situations more explicitly.
# 
# A method refers to a function which is part of a class. You access it with an instance or object of the class. A function doesn’t have this restriction: it just refers to a standalone function. This means that all methods are functions, but not all functions are methods. 

# In[4]:


# stand alone function
sum(x)


# In[5]:


# method 
x.sum(axis = 0)


# As illustrated above, there can be functions and methods that behave in a similar manner. However, often, methods have special parameters that allow them to behave uniquely to the object they are attached to. For example, the `sum()` method for the Numpy array allows you to get the overall sum, sum of each column, and sum of each row. This would take more effort to compute with the stand alone function.

# In[6]:


# overall sum
x.sum()


# In[7]:


# sum of each column
x.sum(axis = 0)


# In[8]:


# sum of each row
x.sum(axis = 1)


# Nonetheless, being able to create stand alone functions is a critical task. And, if you delve into building your own object classes down the road, defining methods is a piece of cake if you know how to define stand alone functions.

# ## Defining functions
# 
# There are four main steps to defining a function:
# 
# 1. Use the keyword `def` to declare the function and follow this up with the function name.
# 2. Add parameters to the function: they should be within the parentheses of the function. End your line with a colon.
# 3. Add statements that the functions should execute.
# 4. End your function with a return statement if the function should output something. Without the return statement, your function will return an object `None`.

# In[9]:


def yell(text):
    new_text = text.upper()
    return new_text
  
yell('hello world!') 


# Of course, your functions will get more complex as you go along: you can add `for` loops, flow control, and more to it to make it more finegrained. Let's build a function that finds the total sales for a store, for a given day. The parameters required for the function are the `data` frame being analyzed, the `store_id`, and the specific `week` for which we need the sales.

# In[10]:


def store_sales(data, store, week):
    filt = (data['store_id'] == store) & (data['week'] == week)
    total_sales = data['sales_value'][filt].sum()
    return total_sales

store_sales(data=df, store=309, week=48)


# ### Knowledge check
# 
# ```{admonition} Tasks:
# :class: attention
# 1. Define a function titled `ratio` that takes arguments `x` and `y` and returns their ratio, $\frac{x}{y}$.
# 2. Now add a third variable `digits` that allows you to round the output to a specified decimal.
# 3. Now set the default to 2.
# ```

# ## Parameters vs arguments
# 
# People often refer to function parameters and arguments synonymously but, technically, they represent two different things. Parameters are the names used when defining a function or a method, and into which arguments will be mapped. In other words, arguments are the things which are supplied to any function or method call, while the function or method code refers to the arguments by their parameter names.
# 
# ```{tip}
# Being specific about the term _'parameters'_ versus _'arguments'_ can be helpful when discussing specific details regarding a function or inputs, especially during debugging.
# ```
# 
# Python accepts a variety of parameter-argument calls. The following discusses some of the more common implementations you'll see.

# ### Keyword arguments
# 
# Keyword arguments are simply named arguments in the function call. Consider our `store_sales()` function, we can specify parameter arguments in two different ways. The first is positional, in which we supply our arguments in the same position as the parameter. However, this is less explicit and if we happen to switch our `store` and `week` argument placement then we may get different results then anticipated.

# In[11]:


# implicitly computing store sales for store 46 during week 43
store_sales(df, 46, 43) 


# In[12]:


# implicitly computing store sales for store 43 (does not exist) during week 46
store_sales(df, 43, 46) 


# Using keyword, rather than positional, arguments makes your function call more explicit and allows you to specify them in different orders.
# 
# ```{tip}
# Per the [Zen of Python](https://www.python.org/dev/peps/pep-0020/), *'explicit is better than implicit'*.
# ```

# In[13]:


# explicitly computing store sales for store 46 during week 43
store_sales(data=df, week=43, store=46) 


# ### Default arguments
# 
# Default arguments are those that take a default value if no argument value is passed during the function call. You can assign this default value by with the assignment operator `=`, just like in the below example. For example, if your analysis routinely analyzes transactions for all quantities but sometimes you only focus on sales for when quantity purchased meets some threshold, you could add a new parameter with a default value.
# 
# ```{note}
# Default arguments should be placed after parameters with no defaults assigned in the function call. 
# ```

# In[14]:


def store_sales(data, store, week, qty_greater_than=0):
    filt = (data['store_id'] == store) & (data['week'] == week) & (data['quantity'] > qty_greater_than)
    total_sales = data['sales_value'][filt].sum()
    return total_sales

# you do not need to specify an input for qty_greater_than
store_sales(data=df, store=309, week=48)


# In[15]:


# but you can if you want to change it from the default
store_sales(data=df, store=309, week=48, qty_greater_than=2)


# ### &#42;args and &#42;&#42;kwargs
# 
# &#42;args and &#42;&#42;kwargs allow you to pass a variable number of arguments to a function. This can be usefule when you do not know before hand how many arguments will be passed to your function by the user or if you want to allow users to pass arguments through to an embedded function. 
# 
# ```{tip}
# Just an FYI that it is not necessary to write &#42;args or &#42;&#42;kwargs. Only the &#42; (asterisk) is necessary. You could have also written &#42;var and &#42;&#42;vars. Writing &#42;args and &#42;&#42;kwargs is just a convention established in the Python community.
# ```
# 
# &#42;args is used to send a non-keyworded variable length argument list to the function. When the function is called, Python collects the &#42;args values as a tuple, which can be used in a similar manner as any other tuple functionality (i.e. indexing, `for` looped) For example, we can let the user supply as many string inputs to the very useful `yell()` function by using &#42;args.

# In[16]:


def yell(*args):
    new_text = ' '.join(args).upper()
    return new_text
  
yell('hello world!', 'I', 'love', 'Python!!')


# The special syntax &#42;&#42;kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. The reason is because the double star allows us to pass through keyword arguments (and any number of them). Python collects the &#42;&#42;kwargs into a new dictionary, which can be used for any normal dictionary functionality.

# In[17]:


# **kwargs just creates a dictionary
def students(**kwargs):
    print(kwargs)
    
students(student1='John', student2='Robert', student3='Sally')


# In[18]:


# we can use this dictionary however necessary
def print_student_names(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')
    
print_student_names(student1='John', student2='Robert', student3='Sally') 


# ### Type hints
# 
# Python 3.5 added a new library called typing that adds [***type hinting***](https://docs.python.org/3/library/typing.html) to Python. Type hinting is part of a larger functionality called Type Checking (see [this tutorial](https://realpython.com/python-type-checking/) for a comprehensive Type Checking guide). Type hinting provides a way to help users better understand what type of arguments a function takes and the expected output. 
# 
# For example, let's look at a simple function:

# In[19]:


def some_function(name, age):
    return f'{name} is {age} years old'
 
some_function('Tom', 27)


# In the above function we simply expect the user to insert the proper type of arguments and to realize the output will be a string. Now, this isn't that challenging because its a small and simple function but as our functions get more complex it is not always easy to decipher what type of arguments should be passed and what the output will be.
# 
# We can hint to the user this information with type hints by re-writing the function as below. Here, we are hinting that the `name` argument should be a string, `age` should be an integer, and the output will be a string (`-> str`).

# In[20]:


def some_function(name: str, age: int) -> str:
    return f'{name} is {age} years old'
 
some_function('Tom', 27)


# Now, when you look at the function documentation, you can quickly see the type hints (we'll see additional ways to improve function documentation in the Docstrings section).
# 

# In[21]:


help(some_function)


# Even better, most IDEs support type hints so that they can give you feedback as you are typing:
# 
# :::{figure-md} type-hints
# <img src="../images/type_hints.png" alt="Type hints" width="65%">
# 
# Type hints often show up when you hover over the function in most IDEs.
# :::
# 
# When declaring types, you can use any of the built-in Python data types. This includes, but is not limited to:
# 
# * `int`, `float`, `str`, `bool`
# * `tuple`, `list`, `set`, `dict`, `array`
# * `frozenset`
# * `Optional`
# * `Iterable`, `Iterator`
# * and many more!
# 
# You can also declare non-built-in data types such as Pandas and Numpy object types. For example, we can re-write our `store_sales()` function with type hints where we hint that `data` should be a `pd.DataFrame`.
# 
# ```{tip}
# Note that `pd.DataFrame` assumes that you imported the Pandas module with the `pd` alias.
# ```

# In[22]:


def store_sales(data: pd.DataFrame, store: int, week: int) -> float:
    filt = (data['store_id'] == store) & (data['week'] == week)
    total_sales = data['sales_value'][filt].sum()
    return total_sales
  
store_sales(data=df, store=309, week=48)


# ### Knowledge check
# 
# ```{admonition} Tasks:
# :class: attention
# 1. Recreate the `ratio` function that takes arguments `x` and `y` and returns their ratio, $\frac{x}{y}$.
# 2. Add a third variable `digits` that allows you to round the output to a specified decimal and set the default to 2.
# 3. Had type hints that specify `x` and `y` to be `float`, `digits` to be `int` and the output returned to be `float`.
# ```

# ## Docstrings
# 
# Type hints are great for guiding users; however, they only provide small hints. Python docstrings are a much more robust way to document a Python function (docstrings can also be used to document modules, classes, and methods). Docstrings are used to provide users with descriptive information about the function, required inputs, expected outputs, example usage and more. Also, it is a common practice to generate online (html) documentation automatically from docstrings using tools such as Sphinx.
# 
# ```{tip}
# See the [Pandas API reference](https://pandas.pydata.org/pandas-docs/stable/reference/index.html) for the various Pandas functions/methods/class for example Sphinx documentation that is built from docstrings.
# ```
# 
# Docstrings typically consist of a multi-line character string description that follows the header line of a function definition. The following provides an example for a simple addition function. Note how the docstring provides a summary of what the function does, information regarding expected parameter inputs, what the returned output will be, a "see also" section that lets users know about related functions/methods (this can be skipped if not applicable), and some examples of implementing the function.

# In[23]:


def store_sales(data: pd.DataFrame, store: int, week: int) -> float:
    """
    Compute total store sales.
    
    This function computes the total sales for a given
    store and week based on a user supplied DataFrame that
    contains sales in a column named `sales_value`.
    
    Parameters
    ----------
    data : DataFrame
        Pandas DataFrame
    store : int
        Integer value representing store number
    week : int
        Integer value representing week of year
    
    Returns
    -------
    float
        A float object representing total store sales
    
    See Also
    --------
    store_visits : Computes total store visits
    
    Examples
    --------
    >>> store_sales(data=df, store=309, week=48)
    395.6
    >>> store_sales(data=df, store=46, week=43)
    60.39
    """
    filt = (data['store_id'] == store) & (data['week'] == week)
    total_sales = data['sales_value'][filt].sum()
    return total_sales


# ```{tip}
# There are some typical Pythonic conventions used when writing docstrings. Rather than reiterate them here, we highly suggest using the [Pandas](https://pandas.pydata.org/pandas-docs/stable/development/contributing_docstring.html) and [Numpy](https://numpydoc.readthedocs.io/en/latest/format.html) docstring guide standards when writing your docstrings.
# ```
# 
# ### Knowledge check
# 
# ```{admonition} Task:
# :class: attention
# Go back to the `ratio` function you created in the last knowledge check and add docstrings. Be sure to include a general description of what the function does, documentation on the parameters and return output, along with including examples.
# ```

# ## Errors and exceptions
# 
# For functions that will be used over and over again, and especially for those used by someone other than the creator of the function, it is good to include procedures to check for errors that may derail function execution. This may include ensuring the user supplies proper argument types, the computation can perform with the values supplied, or even that execution can be performed in a reasonable amount of time. 
# 
# This falls under the umbrella of exception handling and is actually far broader than what we can cover here. In this section, we'll demonstrate some of the basics.
# 

# ### Validating arguments
# 
# A common problem is when the user supplies invalid argument types or values. Although we have seen how to use type hints and docstrings to inform users, we can also include useful exception calls for when users supply improper argument types and values. For example, the following will check if the arguments of the correct type by using `isinstance` and, if they are not, we `raise` an `Exception` and include an informative error.

# In[24]:


def store_sales(data: pd.DataFrame, store: int, week: int) -> float:
     # argument validation
    if not isinstance(data, pd.DataFrame): raise Exception('`data` should be a Pandas DataFrame')
    if not isinstance(store, int): raise Exception('`store` should be an integer')
    if not isinstance(week, int): raise Exception('`week` should be an integer')
  
    # computation
    filt = (data['store_id'] == store) & (data['week'] == week)
    total_sales = data['sales_value'][filt].sum()
    return total_sales
  
store_sales(data=df, store='309', week=48) 


# Note that `Exception()` is used to create a generic exception object/output. Python has [many built-in exception types](https://docs.python.org/3/library/exceptions.html) that can be used to indicate a specific error has occured. For example, we could replace `Exception()` with `TypeError()` in the previous example to make it more specific that the error is due to an invalid argument type.

# In[56]:


def store_sales(data: pd.DataFrame, store: int, week: int) -> float:
    # argument validation
    if not isinstance(data, pd.DataFrame): raise TypeError('`data` should be a Pandas DataFrame')
    if not isinstance(store, int): raise TypeError('`store` should be an integer')
    if not isinstance(week, int): raise TypeError('`week` should be an integer')
  
    # computation
    filt = (data['store_id'] == store) & (data['week'] == week)
    total_sales = data['sales_value'][filt].sum()
    return total_sales
  
store_sales(data=df, store='309', week=48) 


# We can expand this as much as necessary. For example, say we want to ensure users only use a store value that exists in our data. Currently, if the user supplies a store value that does not exist (i.e. 35), they simply get a return value of 0. 

# In[57]:


store_sales(data=df, store=35, week=48)


# We can add an `if` statement to check if the store number exists and supply an error message to the user if it does not:

# In[67]:


def store_sales(data: pd.DataFrame, store: int, week: int) -> float:
    # argument validation
    if not isinstance(data, pd.DataFrame): raise TypeError('`data` should be a Pandas DataFrame')
    if not isinstance(store, int): raise TypeError('`store` should be an integer')
    if not isinstance(week, int): raise TypeError('`week` should be an integer')
    if store not in data.store_id.unique(): 
        raise ValueError(f'`store` {store} does not exist in the supplied DataFrame')
  
  
    # computation
    filt = (data['store_id'] == store) & (data['week'] == week)
    total_sales = data['sales_value'][filt].sum()
    return total_sales

store_sales(data=df, store=35, week=48)


# ### Assert statements
# 
# Python’s `assert` statement is a debugging aid that tests a condition. If the condition is true, it does nothing and your program just continues to execute. But if the assert condition evaluates to false, it raises an `AssertionError` exception with an optional error message. This seems very similar to the example in the last section where we checked if the supplied store ID exists. However, the proper use of assertions is to inform users about unrecoverable errors in a program. They’re not intended to signal expected error conditions, like “store ID not found”, where a user can take corrective action or just try again.
# 
# ```{tip}
# Another way to look at it is to say that assertions are internal self-checks for your program. They work by declaring some conditions as impossible in your code. If one of these conditions doesn’t hold that means there’s a bug in the program.
# ```
# 
# For example, say you have a program that automatically applies a discount to product and you eventually write the following `apply_discount` function:

# In[59]:


def apply_discount(product, discount):
    price = round(product['price'] * (1.0 - discount), 2)
    assert 0 <= price <= product['price']
    return price


# Notice the assert statement in there? It will guarantee that, no matter what, discounted prices cannot be lower than \$0 and they cannot be higher than the original price of the product.
# 
# Let’s make sure this actually works as intended. You can see that the second example throws an `AssertionError`

# In[60]:


# 25% off 3.50 should equal 2.62
milk = {'name': 'Chocolate Milk', 'price': 3.50}
apply_discount(milk, 0.25)


# In[61]:


# 200% discount is not allowed
apply_discount(milk, 2.00)


# In the above example, we simply got an `AssertionError` but no message to help us understand what caused the error. The assert statement follows the syntax of `assert condition, message` so we can add an informative message at the end of our `assert` statement.

# In[62]:


def apply_discount(product, discount):
    price = round(product['price'] * (1.0 - discount), 2)
    assert 0 <= price <= product['price'], 'Invalid discount applied'
    return price
    
apply_discount(milk, 2.00) 


# ### Try and except
# 
# In the prior sections, we looked at ways to identify errors that may occur. The result of our exception handling is to signal an error occurred and stop the program. However, there are often times when we do not want to stop the program. For example, if the program has a database connection that should be closed after execution then we need our program to continue running even if an error occurs to ensure the connection is closed. 
# 
# The `try except` procedure allows us to try execute code. If it works, great! If not, rather than just throw an exception error, we define what the program should continue to do. For example, the following tries the `apply_discount()` function with a pre-defined discount value. If it throws and exception then we adjust the discount value (if discount is greater than 100% of product price we adjust it to the largest acceptable value, if its less than 0 we just set it to 0%).

# In[63]:


# this discount is created somewhere else in the program
discount = 2

# if discount causes an error adjust it
try:
    apply_discount(milk, discount)
except Exception:
    if discount > 1: discount = 0.99
    if discount < 0: discount = 0
    apply_discount(milk, discount)


# The `try except` procedure allows us to include as many `except` statements as necessary for different types of errors (think of them like `elif`s). For example, the following illustrates how we could have different types of code execution for a `TypeError`, a `ValueError`, and then the final `else` statement captures all other errors.
# 
# ```{warning}
# This procedure will run in order, consequently you want to have the most specific exception handlers first followed by more general exception handlers later on.
# ```

# In[69]:


try:
    store_sales(data=df, store=35, week=48)
except TypeError:
    print('do something specific for a `TypeError`')
except ValueError:
    print('do something specific for a `ValueError`')
else:
    print('do something specific for all other errors')


# Lastly, we may have a certain piece of code that we always want to ensure gets ran in a program. For example, we may need to ensure a database connection or file is closed before an error is thrown. The following illustrates how we can add a `finally` at the end of our `try except` procedure. This `finally` will ___always___ be ran. If the code in the `try` clause runs without error, the `finally` code chunk will run _after_ the `try` block. If an error occurse, the `finally` code chunk will run _before_ the relevant `except` code chunk.

# In[70]:


try:
    store_sales(data=df, store=35, week=48)
except TypeError:
    raise
except ValueError:
    raise
finally:
    print('Code to close database connection')


# ### Knowledge check
# 
# ```{admonition} Tasks:
# :class: attention
# Going back to the `ratio` function:
# 1. Add a procdure to validate that `x` and `y` inputs are numeric and `digits` is an integer.
# 2. Add a try and except procedure where if a `TypeError` is thrown for `digits` because it is a float then the `digits` value is rounded to the nearest integer and applied.
# ```

# ## Scoping
# 
# Scoping refers to the set of rules a programming language uses to lookup the value to variables and/or symbols. The following illustrates the basic concept behind the lexical scoping rules that Python follows. In short, Python follows a nested environment structure and uses what is commonly referred to as the ___LEGB___ search rule:
# 
# 1. Search **l**ocal scope first,
# 2. then the local scopes of **e**nclosing functions,
# 3. then the **g**lobal scope,
# 4. and finally the **b**uilt-in scope
# 
# ### Searching for variables
# 
# What exactly does this mean?  A function has its own environment and when you assign an argument in the `def` header of the function, the function creates a separate environment that keeps that variable separate from any variable in the global environment. This is why you can have an `x` variable in the global environment that won't be confused with an `x` variable in your function:

# In[71]:


x = 84

def func(x):
  return x + 1
  
func(x = 50)  


# However, the function environment is only active when called and all function variables are removed from memory after being called. Consequently, you can continue using `x` that is contained in the global environment.

# In[72]:


x


# However, if a variable does not exist within the function, Python will look one level up to see if the variable exists. In this case, since `y` is not supplied in the function header, Python will look in the next environment up (global environment in this case) for that variable:

# In[74]:


y = 'Boehmke'

def func(x):
  return x + ' ' + y
  
func(x = 'Brad') 


# The same will happen if we have nested functions. Python will search in enclosing functions in a hierarchical fashion until it finds the necessary variables. In this convoluted procedure...
# 
# * `y` is a global variable,
# * `x` & `sep` are local variables to the `my_name` function,
# * and `my_paste` has no local variables,
# * the `my_name` function gets `y` from the global environment,
# * and the `my_paste` function gets all its inputs from the `my_name` environment.
# 
# ```{warning}
# We do not recommend that you write functions like this. This is primarily only for explaining how Python searches for information, which can be helpful for debugging.
# ```

# In[80]:


y = 'Boehmke'

def my_name(sep):
    x = 'Brad'
    def my_paste():
        return x + sep + y
    return my_paste()
  
my_name(sep=' ')


# ### Changing variables
# 
# It is possible to change variable values that are outside of the active environment. This is rarely necessary, and is usually not good practice, but it is good to know about. For example, the following changes the global variable `y` by including the keyword-variable statement `global y` prior to making the assignment of the new value for `y`.
# 
# ```{tip}
# The same can be done with changing values in nested functions; however, you would use the keyword `nonlocal` to change the value of an enclosing function's local variable.
# ```

# In[81]:


y = 8451

def convert(x):
    x = str(x)
    firstpart, secondpart = x[:len(x)//2], x[len(x)//2:]
    global y
    y = firstpart + '.' + secondpart
    return y

convert(8451) 


# In[82]:


y


# ## Anonymous functions
# 
# So far we have been discussing defined functions; however, Python allows you to generate _anonymous_ functions on the fly. These are often referred to as __lambdas__.  Lambdas allow for an alternative approach when creating short and simple functions that are only used once or twice. 
# 
# For example, the following two functions are equivalent:
# 
# ```python
# # defined function
# def func(x, y, z):
#     return x + y + z
#   
# # lambda function  
# lambda x, y, z: x + y + z  
# ```
# 
# Note how the `lambda`'s body is a single expression and not a block statement. This is a requirement, which typically restricts lambdas to very short, concise function calls. The best use case for lambda functions are for when you want a simple function to be anonymously embedded within a larger expressions. For example, say we wanted to loop over each item in a list and apply a simple square function, we could accomplish this by supplying a lambda function to the `map` function. `map` just iterates over each item in an object and applies a given function (you could accomplish the exact same with a list comprehension).

# In[83]:


nums = [48, 6, 9, 21, 1]

list(map(lambda x: x ** 2, nums))


# Another good example is the following one you already lesson 6a where we apply a lambda function to assign 'high value' for each transaction where `sales_value` is greater than 10 and 'low value' for all other transactions.

# In[89]:


(
    df['sales_value']
    .apply(lambda x: 'high value' if x > 10 else 'low value')
)


# Here is another example where we group by `basket_id` and then apply a lambda function to compute the average cost per item in each basket.

# In[90]:


(
    df[['basket_id', 'sales_value', 'quantity']]
    .groupby('basket_id')
    .apply(lambda x: (x['sales_value'] / x['quantity']).mean())
)


# ### Knowledge check
# 
# ```{admonition} Task:
# :class: attention
# Let's focus on the transaction timestamp for each transaction (`df['transaction_timestamp']`). Use the `.apply()` method along with a lambda function to assign each transaction to 'weekday' or 'weekend'. To do this check out the `.day_name()` method (i.e. `df['transaction_timestamp'][0].day_name()`)
# ```

# ## Exercises
# 
# ```{admonition} Tasks:
# :class: attention
# 1. Load in the companies.csv data (in the data folder).
# 2. Write a function `is_incorporated` that checks whether an input string, `name`, contains the substring "inc" or "Inc". Its definition should look like this:
#     ```python
#     def is_incorporated(name):
#         ...
# 3. Add type hints and a docstring.
# 4. Test this function to be sure it works. Try passing in some strings that contain the substring and some that don't. Test it on data from the companies DataFrame.
# 5. Write a `for` loop to iterate through the elements in the Name column of the companies data, applying `is_incorporated` to each element and printing the result.
# 5. Now rewrite the code for #4 using the `Series.apply` method -- apply the function to the Series and print the resulting Series.
# ```

# ## Computing environment

# In[ ]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p pandas,jupyterlab,completejourney_py')

