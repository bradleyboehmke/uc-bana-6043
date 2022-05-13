#!/usr/bin/env python
# coding: utf-8

# # Lesson 1b: Variables, operators, and types
# 
# <hr/>

# Whether you are programming in Python or pretty much any other language, you will be working with **variables**.  While the precise definition of a variable will vary from language to language, we'll focus on Python variables here. Like many of the concepts in this class, though, the knowledge you gain about Python variables will translate to other languages.
# 
# We will talk more about **objects** later, but a variable, like everything in Python, is an object. For now, you can think of it this way. The following can be properties of a variable:
# 
# 1. The **type** of variable. E.g., is it an integer, like `2`, or a string, like `'Hello, world.'`?
# 2. The **value** of the variable.
# 
# Depending on the type of the variable, you can do different things to it and other variables of similar type.  This, as with most things, is best explored by example. We'll go through some of the properties of variables and things you can do to them in this tutorial.
# 
# We will work through this and most other modules using Jupyter notebooks. Henceforth in the class, we will use Jupyter notebooks except where explicitly noted. So, launch and notebook, and we'll get rolling!

# ## Learning objectives
# 
# Upon completing this module you will:
# 
# - Understand the primary data types (i.e. integers, floats, strings).
# - Be able to apply different operations (i.e. arithmetic) with these variable types.
# - Know how to assign and evaluate variables.
# - Be able to coherce variables to different types (aka 'type conversion')

# ## Determining the type
# First, we will use Python's built-in `type()` function to determine the type of some variables.

# In[1]:


type(2)


# In[2]:


type(2.3)


# In[3]:


type('Hello, world.')


# The `type` function told us that `2` is an `int` (short for integer), `2.3` is a `float` (short for floating point number, basically a real number that is not an integer), and `'Hello, world.'` is a `str` (short for string). Note that the single quotes around the characters indicate that it is a string. So, `'1'` is a string, but `1` is an integer.
# 
# ```{note}
# We can also express `float`s using scientific notation; $4.5\times 10^{-7}$ is expressed as `4.5e-7`.
# ```

# In[4]:


type(4.5e-7)


# ### A note on strings
# 
# We just saw that strings can be enclosed in single quotes. In Python, we can equivalently enclose them in double quotes. E.g.,
# 
#     'my string'
# 
# and
# 
#     "my string"
# 
# are the same thing. We can also denote a string with triple quotes. So,
# 
#     """my string"""
#     '''my string'''
#     "my string"
#     'my string'
#     
# are all the same thing. 
# 
# ```{tip}
# The difference with triple quotes is that it allows a string to extend over multiple lines.
# ```

# In[5]:


# A multi-line string
my_str = """It was the best of times,
it was the worst of times..."""

print(my_str)


# Note, though, we cannot do this with single quotes.

# In[6]:


# This is a SyntaxError
my_str = 'It was the best of times,
it was the worst of times...'


# ## Operators
# 
# **Operators** allow you to do things with variables, like add them. They are represented by special symbols, like `+` and `*`. For now, we will focus on **arithmetic** operators. Python's arithmetic operators are
# 
# |action|operator|
# |:-------|:----------:|
# |addition | `+`|
# |subtraction | `-`|
# |multiplication | `*`|
# |division | `/`|
# |raise to power | `**`|
# |modulo | `%`|
# |floor division | `//`|
# 
# ```{warning}
# Do not use the `^` operator to raise to a power. That is actually the operator for bitwise XOR, which we will not cover in this class.
# ```

# ### Operations on integers
# 
# Let's see how these operators work on integers.

# In[24]:


2 + 3


# In[25]:


2 - 3


# In[26]:


2 * 3


# In[27]:


2 / 3


# In[28]:


2 ** 3


# In[29]:


2 % 3


# In[30]:


2 // 3


# This is what we would expect. 
# 
# ```{note}
# An important note, though. If you are using Python 2, division of integers defaults to floor division. Some legacy code is written in Python 2, though it officially sunset on New Years Day 2020. Fingers crossed you should not be using Python 2 in a future role!
# ```

# ### Operations on floats
# Let's try floats.

# In[31]:


2.1 + 3.2


# Wait a minute!  We know `2.1 + 3.2 = 5.3`, but Python gives `5.300000000000001`. This is due to the fact that floating point numbers are stored with a finite number of binary bits. There will always be some rounding errors. This means that as far as the computer is concerned, it cannot tell you that `2.1 + 3.2` and `5.3` are equal. This is important to remember when dealing with floats, as we will see in the next lesson.

# In[32]:


2.1 - 3.2


# In[33]:


# Very very close to zero because of finite precision
5.3 - (2.1 + 3.2)


# In[34]:


2.1 * 3.2


# In[35]:


2.1 / 3.2


# In[36]:


2.1 ** 3.2


# In[37]:


2.1 % 3.2


# In[38]:


2.1 // 3.2


# Aside from the floating point precision issue I already pointed out, everything is like we would expect. Note, though, that we cannot divide by zero.

# In[39]:


2.1 / 0.0


# We can't do it with `int`s, either.

# In[40]:


2 / 0


# ### Operations on integers and floats
# 
# This proceeds as we think it should.

# In[41]:


2.1 + 3


# In[42]:


2.1 - 3


# In[43]:


2.1 * 3


# In[44]:


2.1 / 3


# In[45]:


2.1 ** 3


# In[46]:


2.1 % 3


# In[47]:


2.1 ** 3


# And again we have the rounding errors, but everything is otherwise intuitive.

# ### Operations on strings
# 
# Now let's try some of these operations on strings.  This idea of applying mathematical operations to strings seems strange, but let's just mess around and see what we get.

# In[48]:


'Hello, ' + 'world.'


# Ah!  Adding strings together concatenates them! This is also intuitive. How about subtracting strings?

# In[49]:


'Hello, ' - 'world'


# That stands to reason. Subtracting strings does not make sense. The Python interpreter was kind enough to give us a nice error message saying that we can't have a `str` and a `str` operand type for the subtraction operation. It also makes sense that we can't do multiplication, raising of power, etc., with two strings. How about multiplying a string by an integer?

# In[50]:


'Hello, world.' * 3


# Yes, this makes sense! Multiplication by an integer is the same thing as just adding multiple times, so the Python interpreter concatenates the string several times.
# 
# As a final note on operators with strings, watch out for this:

# In[51]:


'4' + '2'


# The result is *not* `6`, but it is a string containing the characters `'4'` and `'2'`.

# ### Order of operations
# 
# The order of operations is also as we would expect. Exponentiation comes first, followed by multiplication and division, floor division, and modulo. Next comes addition and subtraction. In order of precedence, our arithmetic operator table is
# 
# |precedence|operators|
# |:-------:|:----------:|
# |1 | `**`|
# |2 | `*`, `/`, `//`, `%`|
# |3 | `+`, `-`|
# 
# You can also group operations with parentheses. Operations within parentheses is are always evaluated first. Let's practice.

# In[52]:


8 + 9 / 5 ** 2


# In[53]:


8 + 9 / (5 ** 2)


# In[54]:


8 + (9 / 5) ** 2


# In[55]:


(8 + 9) / 5 ** 2


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. Compute one plus 4 squared.
# 2. Compute one plus 4 and then square the output.
# 3. Compute one cubed plus two cubed plus three cubed plus four cubed.
# 4. Compute one plus two plus three plus four and then square the output.
# ```

# ## Variables and assignment operators
# 
# So far, we have essentially just used Python as an oversized desktop calculator. We would really like to be able to think about our computational problems symbolically. We mentioned **variables** at the beginning of the lesson, but in practice we were just using numbers and strings directly. We would like to say that a variable, `a`, represents an integer and another variable `b` represents another integer. Then, we could do things like add `a` and `b`. So, we see immediately that the variables have to have a type associated with them so the Python interpreter knows what to do when we use operators with them. A variable should also have a **value** associated with it, so the interpreter knows, e.g., what to add.
# 
# In order to create, or **instantiate**, a variable, we can use an **assignment operator**. This operator is the equals sign. So, let's make variables `a` and `b` and add them.

# In[56]:


a = 2
b = 3
a + b


# Great!  We get what we expect! And we still have `a` and `b`.

# In[57]:


print('a =', a)


# In[58]:


print('b =', b)


# Now, we might be tempted to say, "`a` is two." No. `a` is not two. `a` is a variable that *has a value of 2*. A variable in Python is not just its value. A variable also carries with it a type. It also has more associated with it under the hood of the interpreter that we will not get into. So, you can think about a variable as a map to an address in RAM (called a **pointer** in computer-speak) that stores information, including a type and a value.

# ### Assignment/increment operators
# 
# Now, let's say we wanted to update the value of `a` by adding `4.1` to it. Python will do some magic for us.

# In[59]:


print(type(a), a)

a = a + 4.1

print(type(a), a)


# We see that `a` was initially an integer with a value of 2. But we added `4.1` to it, so the Python interpreter knew to change its type to a `float` and update its value.
# 
# This operation of updating a value can also be accomplished with an **increment operator**.

# In[60]:


a = 2
a += 4.1
a


# The `+=` operator told the interpreter to take the value of `a` and add `4.1` to it, changing the type of `a` in the intuitive way if need be. The other six arithmetic operators have similar constructions, `-=`, `*=`, `/=`, `//=`, `%=`, and `**=`.

# In[61]:


a = 2
a **= 3
a


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. Assign the values 1000, 5, and 0.05 to variables `D`, `K`, and `h` respectively.
# 2. Compute $2 \times D \times K$.
# 3. Compute $\frac{2 \times D \times K}{h}$.
# 4. Now put this together to compute the Economic Order Quantity, which is $\sqrt{\frac{2 \times D \times K}{h}}$. Save the output as `Q`.
# 5. What is the type and value of `Q`?
# 6. Execute `del Q`. What do you think this does?
# ```

# ## Type conversion
# 
# Suppose you have a variable of one type, and you want to convert it to another. For example, say you have a string, `'42'`, and you want to convert it to an integer. This would happen if you were reading information from a text file, which by definition is full of strings, and you wanted to convert some string to a number. This is done as follows.

# In[62]:


my_str = '42'
my_int = int(my_str)
my_int


# In[63]:


type(my_int)


# Conversely, we can convert an `int` back to a `str`.

# In[64]:


str(my_int)


# ```{note}
# Since we did not assign the output of `str(my_int)` to `my_int`, we did not actually change the variable `my_int` to a string. We simply evaluated the coersed ouput. 
# ```

# When converting a `float` to an `int`, the interpreter does not round the result, but gives the floor.

# In[65]:


int(2.9)


# Also consider our string concatenation warning/example from above:

# In[66]:


print('4' + '2')
print(int('4') + int('2'))


# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# 1. Say you have a 12” pizza. Compute the area of the pizza and assign that value to the variable `area`. Now say the cost of the pizza was $8. Compute the cost per square inch and assign that value to a variable `ppsi`.
# 2. Convert variable `ppsi` to an integer. Now what is the value of `ppsi`.
# 3. Convert variable `ppsi` to a string. Now what is the value of `ppsi`.
# ```
# 

# ## Computing environment

# In[67]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab')

