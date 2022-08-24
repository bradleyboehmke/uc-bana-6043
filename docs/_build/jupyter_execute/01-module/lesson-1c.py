#!/usr/bin/env python
# coding: utf-8

# # Lesson 1c: More operators & conditionals
# 
# <hr/>

# In this lesson, we will examine more operators beyond the arithmetic and assignment operators we have already encountered. We will look at **relational operators**, **identity operators**, and **logical operators**. We'll use these operators in **conditional statements**, which help a program decide what to do in certain situations.
# 
# ## Learning objectives
# 
# By the end of this module you will:
# 
# * Understand a new data type called boolean (`True`, `False`).
# * Be able to compare variables using relational, identity, and logical operators.
# * Be able to apply conditional statements to control the flow of your program.

# ## Boolean
# 
# There is an additional data type we did not mention in the previous lesson -- **Boolean** (`bool`). Boolean data types have two possible values: `True` and `False`. These are important keywords in Python that indicate truth. 

# In[1]:


the_truth = True
the_truth


# In[2]:


type(the_truth)


# In[3]:


lies = False
lies


# In[4]:


type(lies)


# Boolean data types most often come about when we are ***comparing*** objects. For example, we often want to compare if two variables have the same value. As we'll see in the following sections, the outputs of these comparisons are a boolean value.

# ## Relational operators
# 
# Suppose we want to compare the values of two numbers.  We may want to know if they are equal for example. The operator used to test for equality is `==`, an example of a **relational operator** (also called a **comparison operator**).

# ### The equality relational operator
# 
# Let's test out the `==` to see how it works.

# In[5]:


5 == 5


# In[6]:


5 == 4


# ```{note}
# Notice that using the operator gives us a Boolean response (either `True` or `False`).
# ```

# The equality operator, like all relational operators in Python, also works with variables, testing for equality of their *values*. Equality of the variables themselves uses **identity operators**, described [below](#Identity-operators).

# In[7]:


a = 4
b = 5
c = 4

a == b


# In[8]:


a == c


# Now, let's try it out with some floats.

# In[9]:


5.3 == 5.3


# In[10]:


2.1 + 3.2 == 5.3


# Yikes! Python is telling us that `2.1 + 3.2` is not `5.3`. This is floating point arithmetic haunting us. Note that floating point numbers that can be exactly represented with binary numbers do not have this problem.

# In[11]:


2.2 + 3.2 == 5.4


# ```{tip}
# This behavior is unpredictable, so here is a rule -- use the `==` operator sparingly with floats. If you need to do a comparison you can always force rounding to control the floating point precision.
# ```
# 

# In[12]:


# round to one decimal prior to comparison
round(2.1 + 3.2, 1) == 5.3


# ### Other relational operators
# 
# As you might expect, there are other relational operators.  The relational operators are
# 
# |English|Python|
# |:-------|:----------:|
# |is equal to | `==`|
# |is not equal to | `!=`|
# |is greater than | `>`|
# |is less than | `<`|
# |is greater than or equal to | `>=`|
# |is less than or equal to | `<=`|
# 
# We can try some of them out!

# In[13]:


4 < 5


# In[14]:


5.7 <= 3


# In[15]:


'michael jordan' > 'lebron james'


# Whoa. What happened on that last one?  The Python interpreter has weighed in on the debate about the greatest basketball player of all time. It clearly thinks Michael Jordan is better than LeBron James, but that seems kind of subjective. To understand what the interpreter is doing, we need to understand how it compares strings.

# ### A brief aside on Unicode
# 
# In Python, characters are encoded with [Unicode](https://en.wikipedia.org/wiki/Unicode). This is a standardized library of characters from many languages around the world that contains over 100,000 characters. Each character has a unique number associated with it. We can access what number is assigned to a character using Python's built-in `ord()` function.
# 
# ```{tip}
# Here’s a [great blog post](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) on Unicode if you’re interested.
# ```

# In[16]:


ord('a')


# In[17]:


ord('b')


# The relational operators on characters compare the values that the `ord` function returns. So, using a relational operator on `'a'` and `'b'` means you are comparing `ord('a')` and `ord('b')`. When comparing strings, the interpreter first compares the first character of each string. If they are equal, it compares the second character, and so on. So, the reason that `'michael jordan' > 'lebron james'` gives a value of `True` is because `ord('m') > ord('l')`.
# 
# Note that a result of this scheme is that testing for equality of strings means that **all** characters must be equal. This is the most common use case for relational operators with strings.

# In[18]:


'i love this class' == 'i love this class!'


# ### Chaining relational operators
# 
# Python allows chaining of relational operators.

# In[19]:


4 < 6 < 6.1 < 9.3


# In[20]:


4 < 6.1 < 6 < 9.3


# This is convenient do to. However, it is important not to do the following, even though it is legal.
# 
# ```{tip}
# Even though it is legal do not mix the direction of the relational operators. First, it makes reading the code more challenging. Second, you can run into logic trouble because some numbers are never actually compared. For example, in the below case, `5` and `4` are never compared.
# ```

# In[21]:


4 < 6.1 > 5


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. 4k UHD monitors, counterintuitively, have a resolution of 3840x2160. Create two variables, width and height, and store 3840 and 2160 in them (respectively).
# 2. How many total pixels are in a display with this resolution? Hint: fill in the blanks with variable names: pixels = `___` * `___`.
# 3. Programmatically assess if a 4k monitor is greater than 8,000,000 pixels.
# 4. Programmatically assess if a 4k monitor has between 8,000,000 - 9,000,000 pixels.
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_00ix89ko&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_96wpk0y7" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Relational Operators"></iframe>
# ```

# ## Identity operators
# 
# Identity operators check to see if two variables occupy the same space in memory; i.e., they are the same object (we'll learn more about objects as we proceed through the class). This is different from the equality relational operator, `==`, which checks to see if two variables have the same **value**. The two identity operators are in the table below.
# 
# |English|Python|
# |:-------|:----------:|
# |is the same object | **`is`**|
# |is not the same object | **`is not`**|
# 
# That's right. The operators are pretty much the same as English! Let's see these operators in action and get at the difference between `==` and `is`. Let's use the **`is`** operator to investigate how Python stored variables in memory, starting with `float`s.

# In[22]:


a = 5.6
b = 5.6

a == b, a is b


# Even though `a` and `b` have the same value, they are stored in different places in memory. They can occupy the same place in memory if we do a `b = a` assignment.

# In[23]:


a = 5.6
b = a

a == b, a is b


# Because we assigned `b = a`, they necessarily have the same (immutable) value. So, the two variables occupy the same place in memory for efficiency.

# In[24]:


a = 5.6
b = a
a = 6.1

a == b, a is b


# In the last two examples, we see that assigning `b = a`, where `a` is a `float` in this case, means that `a` and `b` occupy the same memory. However, reassigning the value of `a` resulted in the interpreter placing `a` in a new space in memory. We can double check the values.
# 
# Integers sometimes do not behave the same way, however.

# In[25]:


a = 5
b = 5

a == b, a is b


# Even though we assigned `a` and `b` separately, they occupy the same place in memory. This is because Python employs **integer caching** for all integers between `-5` and `256`. This caching does not happen for more negative or larger integers.

# In[26]:


a = 350
b = 350

a is b


# Now, let's look at strings.

# In[27]:


a = 'Hello, world.'
b = 'Hello, world.'

a == b, a is b


# So, even though `a` and `b` have the same *value*, they do not occupy the same place in memory. If we do a `b = a` assignment, we get similar results as with `float`s.

# In[28]:


a = 'Hello, world.'
b = a

a == b, a is b


# Let's try string assignment again with a different string.

# In[29]:


a = 'python'
b = 'python'

a == b, a is b


# Wait a minute! If we choose a string `'python'`, it occupies the same place in memory as another variable with the same value, but that was not the case for `'Hello, world.'`. This is a result of Python also doing [**string interning**](https://en.wikipedia.org/wiki/String_interning) which allows for (sometimes very) efficient string processing. Whether two strings occupy the same place in memory depends on what the strings are.
# 
# The caching and interning might be a problem, but you generally do not need to worry about it for **immutable** variables. Being immutable means that once the variables are created, their values cannot be changed. If we do change the value the variable gets a new place in memory. All variables we've encountered so far, `int`s, `float`s, and `str`s, are immutable. We will encounter mutable data types in future modules, in which case it really *does* matter practically to you as a programmer whether or not two variables are in the same location in memory.
# 
# ```{note}
# If you feel a bit overwhelmed don't worry. As we progress throughout this course you will get a good feel for when to use a comparison operator (i.e. `==`) versus an identify operator (i.e. `is`).
# ```

# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. Let's go back to the previous monitor problem. So, say you have a 4k UHD monitor. Create a variable `your_monitor` = 3840 * 2160).
# 2. Now, say you decide to give me your monitor because you want a new one. Programmatically we can write this as `my_monitor` = `your_monitor`.
# 3. Do our monitor variables have the same value? 
# 4. Are our monitor variables the same object?
# 5. You decide to buy a 4k DCI monitor that has pixesl = 4096 x 2160. Update `your_monitor` accordingly.
# 6. Do our monitor variables still have the same value? 
# 7. Are our monitor variables the same object?
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_z0m141ml&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_diawvmp6" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Identity Operators"></iframe>
# ```

# ## Logical operators
# 
# **Logical operators** can be used to connect relational and identity operators. Python has three logical operators.
# 
# |Logic|Python|
# |:-------|:----------:|
# |AND | `and`|
# |OR | `or`|
# |NOT | `not`|
# 
# The `and` operator means that if both operands are `True`, return `True`. The `or` operator gives `True` if *either* of the operands are `True`. Finally, the `not` operator negates the logical result.
# 
# That might be as clear as mud to you. It is easier to learn this, as usual, by example.

# In[30]:


True and True


# In[31]:


True and False


# In[32]:


True or False


# In[33]:


True or True


# In[34]:


not False and True


# In[35]:


not(False and True)


# In[36]:


not False or True


# In[37]:


not (False or True)


# In[38]:


7 == 7 or 7.6 == 9.1


# In[39]:


7 == 7 and 7.6 == 9.1


# I think these examples will help you get the hang of it. Note that it is important to specify the ordering of your operations, particularly when using the `not` operator.
# 
# Note also that
# 
#     a < b < c
#     
# is equivalent to
# 
#     (a < b) and (b < c)
# 
# With these new types of operators in hand, we can construct a more complete table of operator precedence.
# 
# |precedence|operators|
# |:-------|:----------:|
# |1 | `**`|
# |2 | `*`, `/`, `//`, `%`|
# |3 | `+`, `-`|
# |4 | `<`, `>`, `<=`, `>=`|
# |5 | `==`, `!=`|
# |6 | `=`, `+=`, `-=`, `*=`, `/=`, `**=`, `%=`, `//=`|
# |7 | `is`, `is not`|
# |8 | `and`, `or`, `not`|

# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# Back to our monitor problem. Recall `my_monitor` = 3840 * 2160 and `your_monitor` = 4096 * 2160. 
# 
# Test if...
# 1. Both our monitors have more than 8,000,000 pixels.
# 2. At least one of our monitors has more than 8,500,000 pixels.
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_dh8fdnvj&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_gm7r4hqb" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Logical Operators"></iframe>
# ```

# ## Operators we left out
# 
# We have left out a few operators in Python. Two that we left out are the **membership operators**, `in` and `not in`, which we will visit in a forthcoming lesson. The others we left out are **bitwise operators** and operators on **sets**, which we will not be covering in this class.

# ## The numerical values of True and False
# 
# As we move to conditionals, it is important to take a moment to evaluate the numerical values of the keywords `True` and `False`.  They have numerical values of `1` and `0`, respectively.

# In[40]:


True == 1


# In[41]:


False == 0


# You can do arithmetic on `True` and `False`, but you will get implicit type conversion.

# In[42]:


True + False


# In[43]:


True + True + True


# In[44]:


False + False + False


# In[45]:


type(True + False)


# ```{note}
# We will use this quite a bit in later modules but for now just realize that the integer values associated with Booleans allow us to do arithmetic with this data type.
# ```

# ## Conditionals
# 
# **Conditionals** are used to tell your computer to do a set of instructions depending on whether or not a Boolean is `True`. In other words, we are telling the computer:
# 
#     if something is true:
#         do task a
#     otherwise:
#         do task b
# 
# In fact, the syntax in Python is almost exactly the same. As an example, let's ask whether or not a variable (`x`) is positive or not.

# In[46]:


x = 1

if x > 0:
    print('x is a positive number.')


# The syntax of the `if` statement is apparent in the above example. The Boolean expression, `x > 0`, is called the **condition**. If it is `True`, the indented statement below it is executed. This brings up a very important aspect of Python syntax.
# 
# ```{warning}
# Indentation matters!
# ```
# 
# Any lines with the same level of indentation will be evaluated together.

# In[47]:


if x > 0:
    print('x is a positive number.')
    print('Same level of intentation, so still printed!')


# What happens if `x` is not positive?

# In[48]:


x = -1

if x > 0:
    print('x is a positive number.')


# Nothing is printed. This is because we did not tell Python what to do if the Boolean expression `x > 0` evaluated `False`. We can add that with an `else` **clause** in the conditional.

# In[49]:


x = -1

if x > 0:
    print('x is a positive number.')
else:
    print('x is not a positive number.')


# Great! Now, we have a construction that can choose which action to take depending on a value. But what if we want to add multiple options depending on the value of `x`?  One option is it create a nested if-else statement. So now if x is greater than zero a certain statement is printed but if it is not greater than zero it will enter the second "nested" if-else statement to assess if it is negative or not.

# In[50]:


x = -1

if x > 0:
    print('x is a positive number.')
else:
    if x < 0:
        print('x is a negative number.')
    else:
        print('x is not positive nor negative!')


# Notice that the indentation defines which clause the statement belongs to. E.g., the second `if` statement is executed as part of the first `else` clause.
# 
# While this nesting is very nice, we can be more concise by using an `elif` clause.
# 
# ```{tip}
# When possible, refrain from using nested if-else statements and make your if-else statement flat by incorporating `elif`. This will make your code much easier to read and interpret.
# ```

# In[51]:


x = 0

if x > 0:
    print('x is a positive number.')
elif x < 0:
    print('x is a negative number.')
else:
    print('x is not positive nor negative!')


# ### Inline if/else
# 
# It is not uncommon to see single line `if` statements when dealing with very simple conditions that can be written succinctly. For example, the following:

# In[52]:


words = ["the", "list", "of", "words"]

if len(words) > 10:
    x = "long list"
else:
    x = "short list"

x


# Can be re-written to a single line of code:

# In[53]:


x = "long list" if len(words) > 10 else "short list"
x


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. Fill in the blanks below to print the relevant statement for `x`.
# 2. Can you think of another way to write this conditional statement? 
# 
# ```python
# import random
# 
# random.seed(7)
# x = random.randint(-10, 100)
# 
# __ x ____:
#     print('x is greater than 50')
# __ x ____:
#     print('x less than 50 but still positive')
# __:
#     print('x is negative')
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_nisu8a6z&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_okgncx16" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Conditional Statements"></iframe>
# ```

# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# Now that you know that 4k UHD monitors have 3840 x 2160 pixels and a 4k DCI monitor has 4096 x 2160 pixels, create a conditional statement that will take a given monitor variable (i.e. `my_monitor` = _____ pixels) and test if it is:
# 1. Equal to a 4k UHD monitor. If so, print out 'This monitor is a 4k UHD monitor'.
# 2. Equal to a 4k DCI monitor. If so, print out 'This monitor is a 4k DCI monitor'.
# 3. If it is not equal to either of the above then print out 'This is not a 4k monitor'.
# ```

# ## Computing environment
# 

# In[54]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab')

