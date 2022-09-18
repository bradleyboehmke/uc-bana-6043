#!/usr/bin/env python
# coding: utf-8

# # Lesson 4c: Handling text data
# 
# Dealing with character strings is often under-emphasized in data analysis training. The focus typically remains on numeric values; however, the growth in data collection is also resulting in greater bits of information embedded in text. Consequently, handling, cleaning and processing character strings is becoming a prerequisite in daily data analysis. This lesson is meant to give you the foundation of working with character strings.
# 
# ## Learning objectives
# 
# By the end of this lesson you'll be able to:
# 
# * Perform basic character string manipulations.
# * Use regular expressions to identify and manipulate patterns in character strings.

# ## Prerequisites
# 
# The Python standard library has lots of built-in capabilities to manipulate character strings. Pandas has incorporated many of these capabilities and even expanded upon them. In this lesson, we will demonstrate different character string capabilities with the `.str.xxx()` methods provided by Pandas.
# 
# ```{note}
# Most of the Pandas string methods have a similar standard library method that can be applied to character strings outside of DataFrames. See the [standard library documentation](https://docs.python.org/3/library/string.html) for help.
# ```

# In[1]:


import pandas as pd


# For data, we'll leverage the **completejourney** data. For example, the `products` data within **completejourney** provides various variables (e.g. `product_category` and `product_type`) that contain character strings we may need to clean, normalize, or identify patterns within.

# In[2]:


from completejourney_py import get_data

cj_data = get_data()
products = cj_data['products']
products


# ## String basics
# 
# Basic string manipulation typically includes case conversion, counting characters, and extracting parts of a string. The following will demonstrate some of these basic string methods on a Pandas DataFrame but realize that Pandas provides many more string methods. Refer to the [docs](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html) to learn more about the many string methods.
# 
# ```{admonition} Video 🎥:
# <iframe width="560" height="315" src="https://www.youtube.com/embed/bofaC0IckHo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ```
# 
# ```{tip}
# The string methods provided by Pandas are accessed by appending the object with `.str` followed by another dot and then the specific string method. Think of the term ‘accessor’ as giving the object access to specialized string methods.
# ```

# ### Case conversion
# 
# To change the case of a character string we can use `.str.lower()` and `.str.upper()`:

# In[3]:


products['product_category'].str.lower().head()


# In[4]:


products['product_category'].str.upper().head()


# ### Value counts
# 
# We've already seen this method in a previous lesson but it's worth discussing more. The `value_counts()` method is one of the most valuable methods for string columns. It returns the count of each unique value in the Series and sorts it from most to least common.

# In[5]:


# raw value counts
products['product_category'].value_counts()


# In[6]:


# normalized value counts
products['product_category'].value_counts(normalize=True)


# Note how `value_counts()` does not start with `.str`. This is not a string method but is most commonly used for strings. In fact we can use `value_counts()` for any data type.

# In[7]:


# value counts on date-time data
cj_data['transactions']['transaction_timestamp'].value_counts().head()


# ### Character counts
# 
# We can get the count of the entire character string with `len()`. This returns the total number of characters in a string to include white space and other non-alphanumeric characters.

# In[8]:


products['product_category'].str.len().head()


# Sometimes we only want to understand how many times a particular word, statement, or even particular letters are used. We can do this with the `count()` method. This method becomes more flexible as we introduce regular expressions, which we will get to shortly.
# 
# The below illustrates that we can easily count how many times 'meat' is used in the `product_category` column:

# In[9]:


products['product_category'].str.lower().str.count('meat').sum()


# ### Detecting words
# 
# The `contains()` method returns a boolean whether or not the passed string is contained somewhere within the string. We can use this to filter for particular words or expressions. For example, the following finds all products where `product_category` contains 'meat'.
# 
# ```{tip}
# We can use `case=False` to ignore case sensitivity. We also use `na=False` to fill in all missing `product_category` values with `False`. If we didn't do this then the subsetting would throw an error. However, use this wisely as it is basically treating missing `product_category` values as non-meat products!
# ```

# In[10]:


meat_products = products['product_category'].str.contains('meat', case=False, na=False)
products[meat_products]


# ### Extracting parts of strings
# 
# We can use traditional index-styling to extract or slice parts of a character string. For example, the following gets the first and last 5 characters in each string.

# In[11]:


products['product_category'].str[:5].head()


# In[12]:


products['product_category'].str[-5:].head()


# ### Replacing parts of strings
# 
# Sometimes we may want to clean up character strings by replacing certain words or phrases. For example, this data contains the word ‘frzn’ in place of 'frozen'. If we wanted to fix this we could use the `replace()` method.

# In[13]:


# product_category observations containing 'frzn'
frzn_products = products['product_category'].str.contains('frzn', case=False, na=False)
products[frzn_products].head()


# In[14]:


# replacing 'frzn' with 'frozen' in `product_category` column
products['product_category'] = products['product_category'].str.replace('frzn', 'frozen', case=False)
products[frzn_products].head()


# ### Knowledge check
# 
# ```{admonition} Questions
# :class: attention
# 1. Using the `product_type` column, which product has the longest description? How about the shortest?
# 2. Which `package_size` values are most common in our data? Which is the least common?
# 2. Replace all instances of 'DSH' with 'dish' in the `product_category` column. How many products does this impact?
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_3i8v2g52&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_9vsktndr" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: String basics knowledge check"></iframe>
# ```

# ## Regular expressions
# 
# A regular expression (aka regex) is a sequence of characters that define a search pattern, mainly for use in pattern matching with text strings. Typically, regex patterns consist of a combination of alphanumeric characters as well as special characters. The pattern can also be as simple as a single character or it can be more complex and include several combinations of characters.
# 
# To understand how to work with regular expressions in Python, we need to consider two primary features of regular expressions. One has to do with the syntax, or the way regex patterns are expressed in Python. The other has to do with the functions used for regex matching in Python. You will be exposed to both of these in the following sections.

# ### Regex basics
# 
# Python’s standard library, and Pandas adoption of these string methods provides us a convenient approach to regular expressions. Many of the methods used in the previous sections can be used with regex. The common pattern for our method calls consist of:
# 
# <center>
# <code>string_object.str.*(pattern)</code>
# </center>
# 
# where:
# 
# * `string_object` represents the character string input (i.e. products['product_category']),
# * `.str.*` represents a wide variety of regex methods depending on what you want to do,
# * `pattern` represents the regex pattern you are looking to match.
# 
# For example let’s say you are looking for observations where the word “FRUIT” was used in the `product_category` description. As we saw earlier `.str.contains()` detects the presence or absence of a pattern (“FRUIT” in this example) and returns a boolean response. Since the output is TRUE or FALSE, this is a handy function to combine with indexing to filter for observations that have that pattern.

# In[15]:


# detect if the word "fruit" is used in each comment
fruit_products = products['product_category'].str.contains('fruit', case=False, na=False)
products[fruit_products]


# There are wide variety of `.str.` methods. See the previous sections for some of the more common ones or peruse the Pandas [Working with Text Data documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html) for examples of more.

# ### Multiple words
# 
# In the previous section you saw that you can search for a given word using some of the `.str.` methods. We can build onto this and search for multiple words. For example, you can search for the phrase “summer” or "fall". One may initially think about performing this search with the following in which case we use traditional word matching and then subsetting. This is known as a ‘literal’ search.

# In[16]:


summer_products = products['product_category'].str.contains('summer', case=False, na=False)
fall_products = products['product_category'].str.contains('fall', case=False, na=False)

products[summer_products | fall_products].head()


# This works, but as our searches get more complex this approach become quite tedious. Instead, we can start using regex search patterns to simplify this process.  The below approach will search for observations that include the word “summer”, “fall”, or a combination of the two. This is equivalent to the above statement but more succinct. This is truly a regex, as instead of searching for a literal statement, we are looking for a pattern of of letter/word combinations.

# In[17]:


summer_or_fall = products['product_category'].str.contains('summer|fall', case=False, na=False)
products[summer_or_fall].head()


# We can see that our regex of ‘summer|fall’ returns more observations than our literal search.

# In[18]:


literal_count = products[summer_products | fall_products].shape[0]
regex_count = products[summer_or_fall].shape[0]

print(f'Literal approach: {literal_count} rows')
print(f'Regex approach: {regex_count} rows')


# ### Line anchors
# 
# Line anchors are used to identify patterns at the beginning or end of an element.  To find a pattern at the beginning of the element we use `^` and a pattern at the end of the element is found with `$`.  For example, if you wanted to find any observations with the word "fruit" in the `product_category` column we can use the following as we saw earlier:

# In[19]:


# detect if the word "fruit" is used in each comment
fruit_products = products['product_category'].str.contains('fruit', case=False, na=False)
products[fruit_products].head()


# However, if we only wanted those products where the category starts with “fruit” than we can use the `^` anchor:

# In[20]:


starts_with_fruit = products['product_category'].str.contains('^fruit', case=False, na=False)
products[starts_with_fruit].head()


# Alternatively, if we only wanted those products where the category *ends with* "fruit" than we can use the `$` anchor:
# 

# In[21]:


ends_with_fruit = products['product_category'].str.contains('fruit$', case=False, na=False)
products[ends_with_fruit].head()


# And we can combine the two if we only wanted those products where the category *starts or ends with* "fruit":

# In[22]:


starts_or_ends_with_fruit = (
    products['product_category']
    .str.contains('^fruit|fruit$', case=False, na=False)
)

products[starts_or_ends_with_fruit].head()


# ### Metacharacters
# 
# Metacharacters consist of non-alphanumeric symbols such as: 
# 
# <p>
# <center>
# . &nbsp;&nbsp; &#92; &nbsp;&nbsp; | &nbsp;&nbsp; ( &nbsp;&nbsp; ) &nbsp;&nbsp; [ &nbsp;&nbsp; { &nbsp;&nbsp; $ &nbsp;&nbsp; &#x2A; &nbsp;&nbsp; + &nbsp;&nbsp;?
# </center>
# </p>
# 
# To match metacharacters in regex you need to *escape*. In R, we escape them with a double backslash "\\".  The following displays the general escape syntax for the most common metacharacters:
# 
# ```{list-table} Escaping metacharacters.
# :header-rows: 1
# :name: escaping-characters
# 
# * - Metacharacter
#   - Literal Meaning
#   - Escape Syntax
# * - .
#   - period or dot
#   - `\.`
# * - $
#   - dollar sign
#   - `\$`
# * - &#x2A;
#   - asterisk
#   - `\*`
# * - &plus;
#   - plus sign
#   - `\+`
# * - ?
#   - question mark
#   - `\?`
# * - \|
#   - vertical bar
#   - `\|`
# * - ^
#   - caret
#   - `\^`
# * - [
#   - square bracket
#   - `\[`
# * - {
#   - curly brace
#   - `\{`
# * - (
#   - parenthesis
#   - `\(`
# ```
# The reason we need to escape these characters is because most of these actually have meaning when declaring regular expressions. For example, say we wanted to identify any `product_category` that contains a period ("."). If we simply use the following we actually get ***all*** our records back. 
# 
# ```{warning}
# Actually, this returns ***almost*** all our records. Since we use `na=False`, any `product_category` that has a missing value will be dropped.
# ```

# In[23]:


wildcard = products['product_category'].str.contains('.', case=False, na=False)
products[wildcard].head()


# So, we need to use an **escape** ("\") to tell the regular expression you want to match a literal metacharacter.

# In[24]:


includes_dot = products['product_category'].str.contains('\.', case=False, na=False)
products[includes_dot].head()


# ### Character classes
# 
# To match one of several characters in a specified set we can enclose the characters of concern with square brackets `[ ]`. In addition, to matching any characters __not__ in a specified character set we can include the caret `^` at the beginning of the set within the brackets. The following displays the general syntax for common character classes but these can be altered easily as shown in the examples that follow:
# 
# ```{list-table} Common character classes.
# :header-rows: 1
# :name: common-characters-classes
# 
# * - Character class
#   - Description
# * - `[aeiou]`
#   - match any specified lower case vowel 
# * - `[AEIOU]`
#   - match any specified upper case vowel 
# * - `[0123456789]`
#   - match any specified numeric values 
# * - `[0-9]`
#   - match any range specified numeric values 
# * - `[a-z]`
#   - match any range of lowercase letters 
# * - `[A-Z]`
#   - match any range of uppercase letters 
# * - `[a-zA-Z0-9]`
#   - match any of the above 
# * - `[^aeiou]`
#   - match anything other than a lowercase vowel 
# * - `[^0-9]`
#   - match anything other than the specified numeric values
# ```
# 
# For example, say we wanted to find any products where the `package_size` is not a round numeric size in ounces. The following identifies any rows where `package_size` contains a dot (remember, we need to escape that character with `\.`) followed by "oz".

# In[25]:


decimal_ounces = products['package_size'].str.contains('\.[0-9] oz', case=False, na=False)
products[decimal_ounces].head()


# Now, say we wanted to do the same but we are interested in any packages that are in ounces (“OZ”) or pounds (“LB”). Your first reaction is probably to do something like:

# In[26]:


decimal_ounces_or_lbs = (
    products['package_size']
    .str.contains('\.[0-9] oz|lb', case=False, na=False)
)

products[decimal_ounces_or_lbs].head()


# Wait! The first observation is in pounds but its a round number and not a decimal.  This is because our regex (`\.[0-9] oz|lb`) is actually looking for any package size where its a decimal of ounces (`\.[0-9] oz`) ***or*** in pounds (`lb`). 
# 
# We need to modify our regex just a tad. If we change it to `\.[0-9] (oz|lb)` (note that `oz|lb` is now in parenthesis), we are now specifying to search for `\.[0-9]` followed by "oz" or "lb".
# 
# ```{tip}
# Using parentheses such as `(oz|lb)` is known as grouping. If we simply use `(oz|lb)` then it will be treated as a [capture grouping](https://www.regular-expressions.info/brackets.html) and Pandas will throw a warning letting you know that you could extract the matching groups if you prefer. If this warning bothers you then you can add `?:` at the begining (`(?:oz|lb)`)to tell Pandas that you just care about matching this pattern and not capturing each group to extract.
# ```

# In[27]:


decimal_ounces_or_lbs = (
    products['package_size']
    .str.contains('\.[0-9] (oz|lb)', case=False, na=False)
)

products[decimal_ounces_or_lbs].head()


# Now, say we wanted to find any package size that contains a decimal between 0-.4:

# In[28]:


smaller_sizes = (
    products['package_size']
    .str.contains('\.[0-4] (?:oz|lb)', case=False, na=False)
)

products[smaller_sizes].head()


# ### Shorthand character classes
# 
# Since certain character classes are used often, a series of shorthand character classes are available. For example, rather than use `[0-9]` every time we are searching for a number in a regex, we can use just use `\d` to match any digit. The following are a few of the commonly used shorthand character classes:
# 
# ```{list-table} Common shorthand character classes.
# :header-rows: 1
# :name: common-shorthand-characters
# 
# * - Syntax
#   - Description
# * - `\d`
#   - match any digit
# * - `\D`
#   - match any non-digit
# * - `\s`
#   - match a space character
# * - `\S`
#   - match a non-space character
# * - `\w`
#   - match a word
# * - `\W`
#   - match a non-word
# * - `\b`
#   - match a word boundary
# * - `\B`
#   - match a non-word boundary
# ```
# 
# We can use these to find patterns such as...
# 
# Find all products where the `package_size` starts with a numeric digit:

# In[29]:


starts_with_digit = products['package_size'].str.contains('^\d', case=False, na=False)
products[starts_with_digit].head()


# Or all products where the `package_size` starts with a non-digit:

# In[30]:


starts_with_nondigit = products['package_size'].str.contains('^\D', case=False, na=False)
products[starts_with_nondigit].head()


# ### Repetition
# 
# When we want to match a __certain number__ of characters that meet a certain criteria we can apply repetition operators to our pattern searches. Common repetition operators include:
# 
# ```{list-table} Common repetition operators.
# :header-rows: 1
# :name: common-repitions
# 
# * - Syntax
#   - Description
# * - `.`
#   - wildcard to match **any character once**
# * - `?`
#   - the preceding item is optional and will be matched **at most once**
# * - `*`
#   - the preceding item will be matched **zero or more times**
# * - `+`
#   - the preceding item will be matched **one or more times**
# * - `{n}`
#   - the preceding item will be matched **exactly n times**
# * - `{n,}`
#   - the preceding item will be matched **n or more times**
# * - `{n,m}`
#   - the preceding item will be matched **at least n times but not more than m times**
# ```
# 
# For example, say we want to find all products where the `package_size` contains at least 3 digits:

# In[31]:


three_digits = products['package_size'].str.contains('\d{3,}', na=False)
products[three_digits].head()


# One thing you probably notice is that the above syntax will match three or more digits within the entire character string. But what if we wanted to identify repetition of a pattern sequence. For example, say we wanted to find `product_id`s where the number "8" is repeated. We can use a **[backreference](https://www.regular-expressions.info/backref.html)** to do so. A backreference will match the same text as previously matched within parentheses. So, in this example, we look for any repeated sequences of the number 8 in `product_id`.

# In[32]:


prod_id_8s = products['product_id'].astype(str).str.contains('(8)\\1', na=False)
products[prod_id_8s].head()


# What if we wanted to look for `product_id`s that contain three "8"s in a row then we need to repeat that pattern:

# In[33]:


prod_id_8s = products['product_id'].astype(str).str.contains('(8)\\1{2}', na=False)
products[prod_id_8s].head()


# ### Putting it altogether
# 
# Ok, let's use a few tools we've learned to answer a question we may get asked by our boss. Say we were asked to identify the top 5 products that have the most total sales; however, we only want to focus on those products that weigh 10lbs or more. We can apply the following steps:
# 
# 1. filter for regex `"^\d{2,}(\.)?.*lb"` which means:
#    - `^\d{2,}`: starts with at least 2 numeric digits
#    - `(\.)?.`: followed by an optional decimal
#    - `.*lb`: followed by a character zero or more times
# 2. take the resulting product list and inner join with transactions so we only retain those transactions and products that have a matching product ID in both tables,
# 3. compute total sales grouped by product (here we use product type just to provide us more context over the product ID),
# 4. and then use `nlargest` to get the top 5 `total_sales` values (you could've also used `sort_values()` to get to the same conclusion).

# In[34]:


size_filter = products['package_size'].str.contains('^\d{2,}(\.)?.*lb', case=False, na=False)
(
    products[size_filter]
    .merge(cj_data['transactions'], how='inner', on='product_id')
    .groupby('product_type', as_index=False)
    .agg({'sales_value': 'sum'})
    .nlargest(5, 'sales_value')
)


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. How many `products` contain the word "bulk" in `product_type`?
# 2. How many `products` do not contain punctuation in their `package_size`?
# 3. Find all frozen pizza products. Be careful, this is not straight forward!
# ```

# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_s4gmiwz2&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_twbs6mzp" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Regex knowledge check"></iframe>
# ```

# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# To answer these questions you'll need to use the `products` and `transactions` data frames.
# 
# 1. Identify all different products that contain "pizza" in their `product_type` description. Which product produces the greatest amount of total sales?
# 2. Identify all products that are categorized (`product_category`) as pizza but are considered a snack or appetizer (`product_type`). Which of these products have the most sales (measured by quantity)?
# 3. How many products contain `package_size`s that do not contain a numeric value.
# ```

# ## Computing environment

# In[35]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab,pandas,completejourney_py')

