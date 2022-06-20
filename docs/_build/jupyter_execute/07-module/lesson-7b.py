#!/usr/bin/env python
# coding: utf-8

# # Lesson 7b: First model with scikit-learn
# 
# In this module, we present how to build predictive models on tabular datasets, with only numerical features.
# 
# In particular we will highlight:
# 
# * the scikit-learn API: `.fit(X, y)`/`.predict(X)`/`.score(X, y)`;
# * how to evaluate the generalization performance of a model with a train-test
#   split.

# ## Learning objectives
# 
# By the end of this lesson you will be able to:
# 
# * Explain and implement the `.fit()`, `.predict()`, and `.score()` methods provided by the scikit-learn API.
# * Evaluate the generalization performance of a model with a train-test
#   split.

# ## Data
# 
# We will use the same dataset "adult_census" described in the previous
# lesson. For more details about the dataset see <http://www.openml.org/d/1590>.

# In[1]:


import pandas as pd

adult_census = pd.read_csv("../data/adult-census.csv")


# ## Separating features from target
# 
# Scikit-learn prefers our features ($X$) apart from our target ($y$). Consequently, it's quite common to create separate data objects to hold our feature and target data.
# 
# ```{note}
# Numerical data is the most natural type of data used in machine learning and can (often)  be directly fed into predictive models. Consequently, for this lesson we will use a subset of the original data with only the numerical columns.
# ```
# 
# Here, we create a `target` data object that contains our target variable (`class`) data and a `features` data object that contains all our numeric feature data.

# In[2]:


import numpy as np

# create column names of interest
target_col = "class"
feature_col = adult_census.drop(columns=target_col).select_dtypes(np.number).columns.values


# In[3]:


target = adult_census[target_col]
target


# In[4]:


features = adult_census[feature_col]
features


# In[5]:


print(
    f"The dataset contains {features.shape[0]} samples and "
    f"{features.shape[1]} features"
)


# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention    
# 1. What type of object is the target data set?
# 2. What type of object is the feature data set?
# ```

# ## Fit a model
# 
# We will build a classification model using the "K-nearest neighbors"
# strategy. To predict the target of a new sample, a k-nearest neighbors takes
# into account its `k` closest samples in the training set and predicts the
# majority target of these samples.
# 
# ```{note}
# We use a K-nearest neighbors here. However, be aware that it is seldom useful
# in practice. We use it because it is an intuitive algorithm. In future lessons, we will introduce alternative algorithms.
# ```
# 
# The `.fit` method is called to train the model from the input (features) and target data.

# In[6]:


# to display nice model diagram
from sklearn import set_config
set_config(display='diagram')


# In[7]:


from sklearn.neighbors import KNeighborsClassifier

# 1. define the algorithm
model = KNeighborsClassifier()

# 2. fit the model
model.fit(features, target)


# Learning can be represented as follows:
# 
# :::{figure-md} fit-method
# <img src="../images/api_diagram-predictor.fit.svg" alt="fit method" width="70%">
# 
# `.fit` method representation.
# :::
# 
# The method `fit` is based on two important elements: (i) **learning algorithm**
# and (ii) **model state**. The model state can be used later to either predict (for classifiers and regressors) or transform data (for transformers).

# ```{note}
# Here and later, we use the name `data` and `target` to be explicit. In
# scikit-learn documentation, `data` is commonly named `X` and `target` is
# commonly called`y`.
# ```

# ## Make predictions
# 
# Let's use our model to make some predictions using the same dataset. To predict, a model uses a **prediction function** that will use the input data together with the model states.
# 

# In[8]:


target_predicted = model.predict(features)


# We can illustrate the prediction mechanism as follows:
# 
# :::{figure-md} predict-method
# <img src="../images/api_diagram-predictor.predict.svg" alt="predict method" width="80%">
# 
# `.predict` method representation.
# :::
# 
# To predict, a model uses a prediction method that will use the input data together with the model states. As for the learning algorithm and the model states, the prediction function is specific for each type of model.
# 
# Let’s now have a look at the computed predictions. For the sake of simplicity, we will look at the five first predicted targets.

# In[9]:


target_predicted[:5]


# ...and we can even check if the predictions agree with the real targets:

# In[10]:


# accuracy of first 5 predictions
target[:5] == target_predicted[:5]


# ```{note}
# Here, we see that our model makes a mistake when predicting the third observation.
# ```

# To get a better assessment, we can compute the average accuracy rate.

# In[11]:


(target == target_predicted).mean()


# This result means that the model makes a correct prediction for approximately 85 samples out of 100. Note that we used the same data to train and evaluate our model. Can this evaluation be trusted or is it too good to be true?

# ## Train-test data split
# 
# When building a machine learning model, it is important to evaluate the
# trained model on data that was not used to fit it, as **generalization** is
# our primary concern -- meaning we want a rule that generalizes to new data.
# 
# Correct evaluation is easily done by leaving out a subset of the data when
# training the model and using it afterwards for model evaluation.
# 
# The data used to fit a model is called <b><em>training data</em></b> while the data used to
# assess a model is called <b><em>testing data</em></b>.

# Scikit-learn provides the helper function `sklearn.model_selection.train_test_split` which is used to automatically split the dataset into two subsets.

# In[12]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    features, 
    target, 
    random_state=123, 
    test_size=0.25,
    stratify=target
)


# ```{note}
# In scikit-learn setting the `random_state` parameter allows to get
# deterministic results when we use a random number generator. In the
# `train_test_split` case the randomness comes from shuffling the data, which
# decides how the dataset is split into a train and a test set).
#     
# And as your target becomes more imbalanced it is important to use the `stratify` parameter.
# ```

# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. How many observations are in your train and test data sets?
# 2. What is the proportion of response values in your `y_train` and `y_test`? 
# ```

# Instead of computing the prediction and manually computing the average
# success rate, we can use the method `score`. When dealing with classifiers
# this method returns their performance metric.
# 
# We can illustrate the score mechanism as follows:
# 
# :::{figure-md} score-method
# <img src="../images/api_diagram-predictor.score.svg" alt="score method" width="90%">
# 
# `.score` method representation.
# :::
# 
# The `.score` method is very similar to the `.predict` method; however, it adds one additional step to compare the predictions made to the actual values and then return an accuracy score. Note how below, we use the test data in the `.score` method so that we are scoring our accuracy based on test data (data not used to train our model).

# In[13]:


# 1. define the algorithm
model = KNeighborsClassifier()

# 2. fit the model
model.fit(X_train, y_train)

# 3. score our model on test data
accuracy = model.score(X_test, y_test)

print(f'The test accuracy using {model.__class__.__name__} is {round(accuracy, 4) * 100}%')


# ```{note}
# If we compare with the accuracy obtained by wrongly evaluating the model
# on the training set, we find that this evaluation was indeed optimistic
# compared to the score obtained on a held-out test set.
# 
# This illustrates the importance of always testing the generalization performance of
# predictive models on a different set than the one used to train these models.
# ```

# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# Scikit-learn provides a logistic regression algorithm, which is another type of algorithm for making binary classification predictions. This algorithm is available at `sklearn.linear_model.LogisticRegression`
#     
# Fill in the blanks below to import the `LogisticRegression` module, define the algorithm, fit the model, and score on the test data.
# 
#     ```python
#     # 1. import the LogisticRegression module
#     from sklearn.linear_model import __________
# 
#     # 2. define the algorithm
#     model = __________
# 
#     # 3. fit the model
#     model.fit(______, ______)
# 
#     # 4. score our model on test data
#     model.score(______, ______)
# 
# How does this models performance compare to the `KNeighborsClassifier` results?
# ```

# ## Computing environment

# In[14]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab,pandas,numpy,sklearn')

