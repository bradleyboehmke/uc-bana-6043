#!/usr/bin/env python
# coding: utf-8

# # Statistical Computing
# 
# ```{note}
# This repository contains additional resources for the UC BANA 6043 Statistical Computing course. The following is a truncated syllabus; for the full syllabus along with complete course content please visit the online course content in [Canvas](https://uc.instructure.com/).
# ```
# 
# Welcome to ___Statistical Computing with Python___! This course provides an intensive, hands-on introduction to statistical computing and data science with the Python programming language. You will gain foundational skills in managing data structures, performing data wrangling, computing and visualizing statistical relationships, managing various environments conducive for statistical analysis, and performing machine learning modeling. Most importantly, since this course only has time to introduce foundational skills, much emphasis is placed on giving you a mental model of Python's data science ecosystem so you know how, when, and where to continue advancing your statistical computing capabilities.

# ## Learning objectives
# 
# Upon successfully completing this course, you will:
# 
# * Have a mental model of the Python data science ecosystem: libraries, capabilities, vocabulary, and widely-available Python resources.
# * Have the ability to use Python within both interactive (Jupyter, REPL) and non-interactive (scripts) environments.
# * Be able to perform core data wrangling activities: importing data, reshaping data, transforming data, and exporting data.
# * Be able to compute descriptive statistics and visualize key patterns and relationships with your data.
# * Be exposed to modeling via scikit-learn and discuss the fundamentals of building models in Python.
# * Have the resources and understanding to continue advancing your statistical computing capabilities.
# 
# ```{note}
# This course assumes no prior knowledge of Python. Experience with programming concepts or another programming language will help, but is not required to understand the material.
# ```

# ## Material
# 
# The bulk of the classroom material will be provided via this book, the recorded lectures, and class notes. In some cases there are additional recommended readings, all of which are readily available online.

# ## Class structure
# 
# __Modules__: For this class each module is covered over the course of week. In the "Overview" section for each module you will find overall learning objectives, a short description of the learning content covered in that module, along with all tasks that are required of you for that module (i.e. quizzes, lab). Each module will have two or more primary lessons and associated quizzes along with a lab.
# 
# __Lessons__: For each lesson you will read and work through the tutorial. Short videos will be sprinkled throughout the lesson to further discuss and reinforce lesson concepts. Each lesson will have various "Your Turn" exercises throughout, along with end-of-lesson exercises. I highly recommend you work through these exercises as they will prepare you for the quizzes, labs, and project work.
# 
# __Quizzes__: There will be a short quiz associated with _each lesson_. These quizzes will be hosted in the course website on Canvas. Please check Canvas for due dates for these quizzes.
# 
# __Labs__: There will be a lab associated with _each module_. For these labs students will be guided through a case study step-by-step. The aim is to provide a detailed view on how to manage a variety of complex real-world data; how to convert real problems into data wrangling and analysis problems; and to apply Python to address these problems and extract insights from the data. Submission of these labs will be done through the course website on Canvas. Please check Canvas for due dates for these labs.
# 
# __Project__: The final project is designed for you to put to work the tools and knowledge that you gain throughout this course. This provides you with multiple benefits. 
#    - It will provide you with more experience using data science tools on real life data sets.
#    - It helps you become a self-directed learner. As a data scientist, a large part of your job is to self-direct your learning and interests to find unique and creative ways to find insights in data.
#    - It starts to build your data science portfolio. Establishing a data science portfolio is a great way to show potential employers your ability to work with data.

# ## Schedule
# 
# ```{note}
# See the [Canvas](https://uc.instructure.com/) course webpage for a detailed schedule with due dates for quizzes, labs, etc.
# ```
# 
# | Module        | Description                                                         |
# |:-------------:|:--------------------------------------------------------------------|
# | **1**         | **Starting with the Basics**                                        |
# |               | Introduction to JupyterLab and the notebook environment             |
# |               | Python fundamentals                                                 |
# | **2**         | **Python Data Science Ecosystem & DataFrames**                      |
# |               | Modules, packages, and a preview of Python's data science ecosystem |
# |               | Importing data and working with DataFrames                          |
# | **3**         | **Data Wrangling Part 1**                                           |
# |               | Subsetting and manipulating data                                    |
# |               | Computing summary statistics at different levels                    |
# | **4**         | **Data Wrangling Part 2**                                           |
# |               | Tidying and joining data                                            |
# |               | Handling text data                                                  |
# | **5**         | **Data Visualization**                                              |
# |               | Higher and lower level plotting APIs                                |
# |               | Interactive visualizations                                          |
# | **6**         | **Creating Efficient Code in Python**                               |
# |               | Control statements & iteration                                      |
# |               | Writing functions                                                   |
# | **7**         | **Intro to Machine Learning with Scikit-Learn**                     |
# |               | Basics of the Scikit-learn API                                      |
# |               | Feature engineering and model evaluation/selection                  |

# ## Conventions used in this book
# 
# The following typographical conventions are used in this book:
# 
# * ___strong italic___: indicates new terms,
# * __bold__: indicates package & file names,
# * `inline code`: monospaced highlighted text indicates functions or other commands that could be typed literally by the user,
# * code chunk: indicates commands or other text that could be typed literally by the user

# In[1]:


1 + 2


# In addition to the general text used throughout, you will notice the following cells:
# 
# ```{tip}
# Signifies a tip or suggestion
# ```
# 
# ```{note}
# Signifies a general note
# ```
# 
# ```{warning}
# Signifies a warning or caution
# ```
# 
# ```{admonition} Questions:
# :class: attention
# Knowledge check exercises to gauge your learning progress.
# ```

# ## Feedback
# 
# To report errors or bugs that you find in this course material please post an issue at https://github.com/bradleyboehmke/uc-bana-6043/issues. For all other communication be sure to use Canvas or the university email. 
# 
# ```{note}
# When communicating with me via email, please always include **BANA6043** in the subject line.
# ```

# ## Acknowledgements
# 
# This course and its materials have been influenced by the following resources:
# 
# * Ethan Swan, [Python for Data Science](https://ethanswan.com/courses/pages/python-for-ds-course)
# * Justin Bois, [Caltech Intro to Programming for the Biological Sciences Bootcamp](https://github.com/justinbois/bootcamp)
# * Tomas Beuzen, [Python Programming for Data Science](https://www.tomasbeuzen.com/python-programming-for-data-science/README.html)
# * Inria, [About Machine learning in Python with scikit-learn MOOC](https://github.com/INRIA/scikit-learn-mooc)
