#!/usr/bin/env python
# coding: utf-8

# # Lesson 7c: Feature Engineering
# 
# Data preprocessing and engineering techniques generally refer to the addition, deletion, or transformation of data. The time spent on identifying data engineering needs can be significant and requires you to spend substantial time understanding your data…or as Leo Breiman said *“live with your data before you plunge into modeling”* ([Breiman 2001](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full)).
# 
# In this lesson, we start introducing a few fundamental feature engineering tasks that can:
# 
# * improve the performance of your numerical features,
# * allow you to include non-numeric features in your modeling,
# * create a scikit-learn pipeline to chain preprocessing and model training steps.

# ## Learning objectives
# 
# By the end of this lesson you'll be able to:
# 
# * Standardize numeric features
# * Pre-process nominal and ordinal features
# * Create a scikit-learn pipeline to chain together feature engineering and model training steps
# * Combine numeric and non-numeric feature engineering steps

# ## Basic prerequisites
# 
# Let's go ahead and import a couple required libraries and import our data. 
# 
# ```{note}
# We will import additional libraries and functions as we proceed but we do so at the time of using the libraries and functions as that will help you to connect specific steps to particular modules/functions imported.
# ```

# In[1]:


import pandas as pd

# to display nice model diagram
from sklearn import set_config
set_config(display='diagram')

# import data
adult_census = pd.read_csv('../data/adult-census.csv')

# separate feature & target data
target = adult_census['class']
features = adult_census.drop(columns='class')


# ## Selection based on data types
# 
# Typically, data types fall into two categories:
# 
# * __Numeric__: a quantity represented by a real or integer number.
# * __Categorical__: a discrete value, typically represented by string labels (but not only) taken from a finite list of possible choices.

# In[2]:


features.dtypes


# ```{note}
# Do not take dtype output at face value! It is possible to have categorical data represented by numbers (i.e. `education_num`. And `object` dtypes can represent data that would be better represented as continuous numbers (i.e. dates).
# 
# Bottom line, always understand how your data is representing your features!
# ```

# We can separate categorical and numerical variables using their data types to identify them.
# 
# There are a few ways we can do this. Here, we make use of [`make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html) helper to select the corresponding columns.

# In[3]:


from sklearn.compose import make_column_selector as selector

# create selector object based on data type
numerical_columns_selector = selector(dtype_exclude=object)
categorical_columns_selector = selector(dtype_include=object)

# get columns of interest
numerical_columns = numerical_columns_selector(features)
categorical_columns = categorical_columns_selector(features)

# results in a list containing relevant column names
numerical_columns


# ## Preprocessing numerical data

# Scikit-learn works "out of the box" with numeric features. However, some algorithms make some assumptions regarding the distribution of our features.
# 
# We see that our numeric features span across different ranges:

# In[4]:


numerical_features = features[numerical_columns]
numerical_features.describe()


# Normalizing our features so that they have mean = 0 and standard deviation = 1, helps to ensure our features align to algorithm assumptions.
# 
# ```{tip}
# Here are a couple reasons for scaling features:
# 
# * Models that rely on the distance between a pair of samples, for instance
# k-nearest neighbors, should be trained on normalized features to make each
# feature contribute approximately equally to the distance computations.
# * Many models such as logistic regression use a numerical solver (based on
# gradient descent) to find their optimal parameters. This solver converges
# faster when the features are scaled.
# ```

# Whether or not a machine learning model requires normalization of the features depends on the model family. Linear models such as logistic regression generally benefit from scaling the features while other models such as tree-based models (i.e. decision trees, random forests) do not need such preprocessing (but will not suffer from it).

# We can apply such normalization using a scikit-learn transformer called [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html).

# In[5]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(numerical_features)


# The `fit` method for transformers is similar to the `fit` method for
# predictors. The main difference is that the former has a single argument (the
# feature matrix), whereas the latter has two arguments (the feature matrix and the
# target).
# 
# :::{figure-md} transformer-fit-method
# <img src="../images/api_diagram-transformer.fit.svg" alt="transfomer.fit method" width="70%">
# 
# `transformer.fit` method representation.
# :::

# In this case, the algorithm needs to compute the mean and standard deviation
# for each feature and store them into some NumPy arrays. Here, these
# statistics are the model states.
# 
# ```{note}
# The fact that the model states of this scaler are arrays of means and
# standard deviations is specific to the `StandardScaler`. Other
# scikit-learn transformers will compute different statistics and store them
# as model states, in the same fashion.
# ```
# 

# We can inspect the computed means and standard deviations.

# In[6]:


scaler.mean_


# In[7]:


scaler.scale_


# ```{tip}
# Scikit-learn convention: if an attribute is learned from the data, its name
# ends with an underscore (i.e. `_`), as in `mean_` and `scale_` for the
# `StandardScaler`.
# ```

# Once we have called the `fit` method, we can perform the data transformation by
# calling the method `transform`.

# In[8]:


numerical_features_scaled = scaler.transform(numerical_features)
numerical_features_scaled


# Let's illustrate the internal mechanism of the `transform` method and put it
# to perspective with what we already saw with predictors.
# 
# :::{figure-md} transformer-transform-method
# <img src="../images/api_diagram-transformer.transform.svg" alt="transfomer.transform method" width="80%">
# 
# `transformer.transform` method representation.
# :::
# 
# The `transform` method for transformers is similar to the `predict` method
# for predictors. It uses a predefined function, called a **transformation
# function**, and uses the model states and the input data. However, instead of
# outputting predictions, the job of the `transform` method is to output a
# transformed version of the input data.

# Finally, the method `fit_transform` is a shorthand method to call
# successively `fit` and then `transform`.
# 
# :::{figure-md} transformer-fit_transform-method
# <img src="../images/api_diagram-transformer.fit_transform.svg" alt="transfomer.fit_transform method" width="80%">
# 
# `transformer.fit_transform` method representation.
# :::

# In[9]:


# fitting and transforming in one step
scaler.fit_transform(numerical_features)


# Notice that the mean of all the columns is close to 0 and the standard deviation in all cases is close to 1:

# In[10]:


numerical_features = pd.DataFrame(
    numerical_features_scaled,
    columns=numerical_columns
)

numerical_features.describe()


# ## Model pipelines

# We can easily combine sequential operations with a scikit-learn
# [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html), which chains together operations and is used as any other
# classifier or regressor. The helper function [`make_pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline) will create a
# `Pipeline`: it takes as arguments the successive transformations to perform,
# followed by the classifier or regressor model.

# In[11]:


from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

model = make_pipeline(StandardScaler(), LogisticRegression())
model


# Let's divide our data into train and test sets and then apply and score our logistic regression model:

# In[12]:


from sklearn.model_selection import train_test_split

# split our data into train & test
X_train, X_test, y_train, y_test = train_test_split(numerical_features, target, random_state=123)

# fit our pipeline model
model.fit(X_train, y_train)

# score our model on the test data
model.score(X_test, y_test)


# ## Preprocessing categorical data

# Unfortunately, Scikit-learn does not accept categorical features in their raw form. Consequently, we need to transform them into numerical representations.
# 
# The following presents typical ways of dealing with categorical variables by encoding them, namely **ordinal encoding** and **one-hot encoding**.

# ### Encoding ordinal categories
# 
# The most intuitive strategy is to encode each category with a different
# number. The [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html) will transform the data in such manner.
# We will start by encoding a single column to understand how the encoding
# works.

# In[13]:


from sklearn.preprocessing import OrdinalEncoder

# let's illustrate with the 'education' feature
education_column = features[["education"]]

encoder = OrdinalEncoder()
education_encoded = encoder.fit_transform(education_column)
education_encoded


# We see that each category in `"education"` has been replaced by a numeric
# value. We could check the mapping between the categories and the numerical
# values by checking the fitted attribute `categories_`.

# In[14]:


encoder.categories_


# ```{note}
# `OrindalEncoder` transforms the category value into the corresponding index value of `encoder.categories_`
# ```

# However, be careful when applying this encoding strategy:
# using this integer representation leads downstream predictive models
# to assume that the values are ordered (0 < 1 < 2 < 3... for instance).
# 
# By default, `OrdinalEncoder` uses a lexicographical strategy to map string
# category labels to integers. This strategy is arbitrary and often
# meaningless. For instance, suppose the dataset has a categorical variable
# named `"size"` with categories such as "S", "M", "L", "XL". We would like the
# integer representation to respect the meaning of the sizes by mapping them to
# increasing integers such as `0, 1, 2, 3`.
# However, the lexicographical strategy used by default would map the labels
# "S", "M", "L", "XL" to 2, 1, 0, 3, by following the alphabetical order.

# The `OrdinalEncoder` class accepts a `categories` argument to
# pass categories in the expected ordering explicitly (`categories[i]` holds the categories expected in the ith column).

# In[15]:


ed_levels = [' Preschool', ' 1st-4th', ' 5th-6th', ' 7th-8th', ' 9th', ' 10th', ' 11th', 
             ' 12th', ' HS-grad', ' Prof-school', ' Some-college', ' Assoc-acdm', 
             ' Assoc-voc', ' Bachelors', ' Masters', ' Doctorate']

encoder = OrdinalEncoder(categories=[ed_levels])
education_encoded = encoder.fit_transform(education_column)
education_encoded


# In[16]:


encoder.categories_


# If a categorical variable does not carry any meaningful order information
# then this encoding might be misleading to downstream statistical models and
# you might consider using one-hot encoding instead (discussed next).

# ### Ecoding nominal categories
# 
# [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) is an alternative encoder that converts the categorical levels into new columns.
# 
# We will start by encoding a single feature (e.g. `"education"`) to illustrate
# how the encoding works.

# In[17]:


from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse=False)
education_encoded = encoder.fit_transform(education_column)
education_encoded


# ```{note}
# `sparse=False` is used in the `OneHotEncoder` for didactic purposes, namely
# easier visualization of the data.
# 
# Sparse matrices are efficient data structures when most of your matrix
# elements are zero. They won't be covered in detail in this workshop. If you
# want more details about them, you can look at [this](https://scipy-lectures.org/advanced/scipy_sparse/introduction.html#why-sparse-matrices).
# ```

# Viewing this as a data frame provides a more intuitive illustration:

# In[18]:


feature_names = encoder.get_feature_names_out(input_features=["education"])
pd.DataFrame(education_encoded, columns=feature_names)


# As we can see, each category (unique value) became a column; the encoding
# returned, for each sample, a 1 to specify which category it belongs to.

# Let's apply this encoding to all the categorical features:

# In[19]:


# get all categorical features
categorical_features = features[categorical_columns]

# one-hot encode all features
categorical_features_encoded = encoder.fit_transform(categorical_features)

# view as a data frame
columns_encoded = encoder.get_feature_names_out(categorical_features.columns)
pd.DataFrame(categorical_features_encoded, columns=columns_encoded).head()


# ```{warning}
# One-hot encoding can significantly increase the number of features in our data. In this case we went from 8 features to 102! If you have a data set with many categorical variables and those categorical variables in turn have many unique levels, the number of features can explode. In these cases you may want to explore ordinal encoding or some other alternative.
# ```

# ### Choosing an encoding strategy
# 
# Choosing an encoding strategy will depend on the underlying models and the
# type of categories (i.e. ordinal vs. nominal).
# 
# ```{tip}
# In general `OneHotEncoder` is the encoding strategy used when the
# downstream models are **linear models** while `OrdinalEncoder` is often a
# good strategy with **tree-based models**.
# ```

# Using an `OrdinalEncoder` will output ordinal categories. This means
# that there is an order in the resulting categories (e.g. `0 < 1 < 2`). The
# impact of violating this ordering assumption is really dependent on the
# downstream models. Linear models will be impacted by misordered categories
# while tree-based models will not.
# 
# You can still use an `OrdinalEncoder` with linear models but you need to be
# sure that:
# - the original categories (before encoding) have an ordering;
# - the encoded categories follow the same ordering than the original
#   categories.
# 
# One-hot encoding categorical variables with high cardinality can cause 
# computational inefficiency in tree-based models. Because of this, it is not recommended
# to use `OneHotEncoder` in such cases even if the original categories do not 
# have a given order.

# ## Using numerical and categorical variables together
# 
# Now let's look at how to combine some of these tasks so we can preprocess both numeric and categorical data.
# 
# First, let's get our train & test data established:

# In[20]:


# drop the duplicated column `"education-num"` as stated in the data exploration notebook
features = features.drop(columns='education-num')

# create selector object based on data type
numerical_columns_selector = selector(dtype_exclude=object)
categorical_columns_selector = selector(dtype_include=object)

# get columns of interest
numerical_columns = numerical_columns_selector(features)
categorical_columns = categorical_columns_selector(features)

# split into train & test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, random_state=123)


# Scikit-learn provides a [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html) class which will send specific
# columns to a specific transformer, making it easy to fit a single predictive
# model on a dataset that combines both kinds of variables together.
# 
# We first define the columns depending on their data type:
# 
# * **one-hot encoding** will be applied to categorical columns. 
# * **numerical scaling** numerical features which will be standardized.
# 
# We then create our `ColumnTransfomer` by specifying three values:
# 
# 1. the preprocessor name, 
# 2. the transformer, and 
# 3. the columns.
# 
# First, let's create the preprocessors for the numerical and categorical
# parts.

# In[21]:


categorical_preprocessor = OneHotEncoder(handle_unknown="ignore")
numerical_preprocessor = StandardScaler()


#  
# <div class="admonition tip alert alert-warning">
#     <p class="first admonition-title" style="font-weight: bold;"><b>Tip</b></p>
#     <p class="last">We can use the <tt class="docutils literal">handle_unknown</tt> parameter to ignore rare categories that may show up in test data but were not present in the training data.</p>
# </ul>
# </div>

# Now, we create the transformer and associate each of these preprocessors
# with their respective columns.

# In[22]:


from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer([
    ('one-hot-encoder', categorical_preprocessor, categorical_columns),
    ('standard_scaler', numerical_preprocessor, numerical_columns)
])


# We can take a minute to represent graphically the structure of a
# `ColumnTransformer`:
# 
# :::{figure-md} ColumnTransformer
# <img src="../images/api_diagram-columntransformer.svg" alt="ColumnTransformer" width="100%">
# 
# `ColumnTransformer` representation.
# :::

# A `ColumnTransformer` does the following:
# 
# * It **splits the columns** of the original dataset based on the column names
#   or indices provided. We will obtain as many subsets as the number of
#   transformers passed into the `ColumnTransformer`.
# * It **transforms each subset**. A specific transformer is applied to
#   each subset: it will internally call `fit_transform` or `transform`. The
#   output of this step is a set of transformed datasets.
# * It then **concatenates the transformed datasets** into a single dataset.
# 
# The important thing is that `ColumnTransformer` is like any other
# scikit-learn transformer. In particular it can be combined with a classifier
# in a `Pipeline`:

# In[23]:


model = make_pipeline(preprocessor, LogisticRegression(max_iter=500))
model


# ```{warning}
# Including non-scaled data can cause some algorithms to iterate
# longer in order to converge. Since our categorical features are not scaled it's often recommended to increase the number of allowed iterations for linear models.
# ```

# In[24]:


# fit our model
_ = model.fit(X_train, y_train)

# score on test set
model.score(X_test, y_test)


# ## Wrapping up

# Unfortunately, we only have time to scratch the surface of feature engineering in this lesson. However, this module should provide you with a strong foundation of how to apply the more common feature preprocessing tasks.
# 
# ```{tip}
# Scikit-learn provides many feature engineering options. Learn more here: https://scikit-learn.org/stable/modules/preprocessing.html
# ```

# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# Using the **ames_clean.csv** data:
# 
# * Numeric features:
#     * Select `GrLivArea` and `YearBuilt` for features and `SalePrice` for the target
#     * Create a train-test split and use `random_state=123`
#     * Create a model pipeline that applies `StandardScaler()` to the features and then applies a [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn-linear-model-linearregression) model.
#     * What is the score for this model based on the test data?
# * Adding a categorical feature:
#     * Select `GrLivArea`, `YearBuilt`, and `Neighborhood` for features and `SalePrice` for the target
#     * Create a train-test split and use `random_state=123`
#     * Create a `ColumnTransformer` object that applies `StandardScaler()` to the numeric features and `OneHotEncoder` to the categorical feature.
#     * Create a model pipeline that combines the `ColumnTransformer` object with a `LinearRegression` model.
#     * What is the score for this model based on the test data?
# ```

# ## Computing environment

# In[25]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab,pandas,sklearn')

