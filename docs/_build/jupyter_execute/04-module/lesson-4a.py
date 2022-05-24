#!/usr/bin/env python
# coding: utf-8

# # Lession 4a: Tidy data
# 
# [Tidy data](https://vita.had.co.nz/papers/tidy-data.pdf) is about “linking the structure of a dataset with its semantics (its meaning)”. It is defined by:
# 
# 1. Each variable forms a column
# 2. Each observation forms a row
# 3. Each type of observational unit forms a table
# 
# Often you’ll need to reshape a dataframe to make it tidy (or for some other purpose).
# 
# <center>
# <img src="https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/tidy.png?raw=true" alt="tidy-data" width="80%" height="80%">
# </center>
# 
# Source: [R4DS](https://r4ds.had.co.nz/tidy-data.html#fig:tidy-structure)
# 
# Once a DataFrame is tidy, it becomes much easier to compute summary statistics, join with other datasets, visualize, apply machine learning models, etc. In this lesson we will focus on ways to reshape DataFrames so that they meet the tidy guidelines.

# ## Learning objectives
# 
# By the end of this lesson you will be able to:
# 
# - Reshape data from wide to long
# - Reshape data from long to wide

# ## Tools for reshaping
# 
# Pandas provides multiple methods that help to reshape DataFrames:
# 
# * `.melt()`: make wide data long.
# * `.pivot()`: make long data width.
# * `.pivot_table()`: same as `.pivot()` but can handle multiple indexes.
# 
# <center>
# <img src="https://github.com/bradleyboehmke/uc-bana-6043/blob/main/book/images/melt_pivot.gif?raw=true" alt="melt-pivot" width="60%" height="60%">
# </center>
# 
# Source: [Garrick Aden-Buie](https://github.com/gadenbuie/tidyexplain#spread-and-gather)
# 
# The following will illustrate each of these for their unique purpose.

# ## Melting wide data
# 
# The below data shows how many homes were sold within each neighborhood across the different years. Is this considered 'tidy data'?  No because we have a variable (year sold) that is represented as the columns and another variable (number of homes sold) filled in as the element values. 
# 
# If you wanted to answer questions like: “Does the number of homes sold vary depending on year?” then the below data is not in the appropriate form to answer this question.

# In[1]:


import pandas as pd

ames_wide = pd.read_csv('../data/ames_wide.csv')
ames_wide.head()


# In this example we would consider this data "wide" and our objective is to convert it into a DataFrame with three variables:
# 
# 1. neighborhood
# 2. year
# 3. homes_sold
# 
# To do so we'll use the `.melt()` method. `.melt()` arguments include:
# 
# - `id_vars`: Identifier column
# - `var_name`: Name to give the new variable represented by the old column headers
# - `value_name`: Name to give the new variable represented by the old element values

# In[2]:


ames_melt = ames_wide.melt(id_vars='neighborhood', var_name='year', value_name='homes_sold')
ames_melt


# The `value_vars` argument allows us to select which specific variables we want to “melt” (if you don’t specify `value_vars`, all non-identifier columns will be used). For example, below I’m omitting the 2006 column:

# In[3]:


ames_wide.melt(
    id_vars='neighborhood',
    value_vars=['2007', '2008', '2009', '2010'], 
    var_name='year', 
    value_name='homes_sold'
    )


# ## Pivoting long data
# 
# Sometimes, you want to make long data wide, which we can do with `.pivot()`. When using `.pivot()` we need to specify the index to pivot on, and the columns that will be used to make the new columns of the wider dataframe. Let's convert our `ames_melt` DataFrame back to the wide format:

# In[4]:


ames_pivot = ames_melt.pivot(index='neighborhood', columns='year', values='homes_sold')
ames_pivot


# You’ll notice that Pandas set our specified index as the index of the new DataFrame and preserved the label of the columns. We can easily remove these names and reset the index to make our DataFrame look like it originally did:

# In[5]:


ames_pivot = ames_pivot.reset_index()
ames_pivot.columns.name = None
ames_pivot


# ## Pivoting with special needs
# 
# `.pivot()` will often get you what you want, but it won’t work if you want to:
# 
# * Use multiple indexes or
# * Have duplicate index/column labels
# 
# For example, let's look at pivoting the below data:

# In[6]:


ames2 = pd.read_csv('../data/ames_wide2.csv')
ames2


# In this example, say you wanted to pivot `ames_wide2` so that the `year_sold` is represented as columns and `homes_sold` values are the elements. If we try to do this similar to the last section's example we get an error stating `ValueError: Index contains duplicate entries, cannot reshape`.

# In[7]:


ames2.pivot(index='neighborhood', columns='year_sold', values='homes_sold')


# The reason is we have duplicate values in our neighborhood column and Pandas doesn't know how to isolate the index values to properly align the pivoted data. In such a case, we’d use `.pivot_table()`. It will apply an aggregation function to our duplicates, in this case, we’ll `sum()` them up:

# In[42]:


ames2.pivot_table(index='neighborhood', columns='year_sold', values='homes_sold', aggfunc='sum')


# If we wanted to keep the numbers per bedroom, we could specify both `neighborhood` and `bedrooms` as multiple indexes:

# In[43]:


ames2.pivot(index=['neighborhood', 'bedrooms'], columns='year_sold', values='homes_sold')


# The result above is a mutlti-index or “hierarchically indexed” DataFrame, which we haven't really talked about up to this point. However, we can easily flatten this with `.reset_index()` and removing the column's index name.

# In[45]:


ames2_reshaped = (
    ames2
    .pivot(index=['neighborhood', 'bedrooms'], columns='year_sold', values='homes_sold')
    .reset_index()
)
ames2_reshaped.columns.name = None
ames2_reshaped.head()


# ## Exercises
# 
# For this exercise, we're going to work with this data set from this paper by [Reeves, et al.](https://www.cell.com/developmental-cell/fulltext/S1534-5807(11)00573-9?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS1534580711005739%3Fshowall%3Dtrue) in which they measured the width of the gradient in the morphogen Dorsal in Drosophila embryos for various genotypes using different method. Don't get hung up in what this means, our object is to simply tidy this dataset.

# In[49]:


df = pd.read_csv("../data/reeves_gradient_width_various_methods.csv", comment='#', header=[0,1])
df


# As can happen with spreadsheets, we have a multiindex, where we have three main groups:
# 
# * `wt` which refers to wild type
# * `dl1/+; dl-venus/+` which we'll refer to as simply Venus 
# * `	dl1/+; dl-gfp/+` which we'll refer to as simply GFP
# 
# For each of these main groups we have multiple sub-columns: two for wild type (`wholemounts`, `cross-sections`), three for Venus (`anti-Dorsal`, `Anti-Venus`, `Venus (live)`), and three for GFP (`anti-Dorsal`, `anti-GFP`, `GFP (live)`). The rows here are the gradient width values recorded for each of the categories. Clearly these data are not tidy.
# 
# For this exercise your objective is to:
# 
# 1. Reshape this data so that it looks like the following:

# In[52]:


expected_result = pd.read_csv('../data/tidy_reeves_gradients.csv')
expected_result


# 2\. Now that you have a tidy data frame you will notice that you have many `NaN`s in the `gradient width` column because there were many of them in the data set. Drop all observations that contain `NaN` values.
# 
# 3\. Now compute summary statistics via `.describe()` for the `gradient width` variable grouped by `genotype` and `method`. Which `genotype` and `method` has the narrowest `gradient width`?

# ## Computing environment

# In[ ]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab,pandas')

