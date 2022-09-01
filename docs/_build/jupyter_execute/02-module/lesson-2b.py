#!/usr/bin/env python
# coding: utf-8

# # Lesson 2b: Importing data
# 
# This lesson introduces you to importing tabular data with Pandas. It also illustrates how you can interact with relational databases via SQL along with how to import common non-tabular data such as JSON and pickle files.

# ## Learning objectives
# 
# By the end of this lesson you will be able to:
# 
# 1. Describe how imported data affects computer memory.
# 2. Import tabular data with Pandas.
# 3. Assess DataFrame attributes and methods.
# 4. Import alternative data files such as SQL tables, JSON, and pickle files.

# ## Data & memory
# 
# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_uqbow9a8&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_oav7kdli" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Data importing framework"></iframe>
# ```
# 
# Python stores its data in memory - this makes it relatively quickly accessible but can cause size limitations in certain fields. In this class we will mainly work with small to moderate data sets, which means we should not run into any space limitations. 
# 
# ```{note}
# Python does provide tooling that allows you to work with _big data_ via distributed data (i.e. [Pyspark](http://spark.apache.org/docs/2.0.0/api/python/index.html)) and relational databrases (i.e. SQL). 
# ```
# 
# Python memory is session-specific, so quitting Python (i.e. shutting down JupyterLab) removes the data from memory. A general way to conceptualize data import into and use within Python:
# 
# 1. Data sits in on the computer/server - this is frequently called "disk"
# 2. Python code can be used to copy a data file from disk to the Python session's memory
# 3. Python data then sits within Python's memory ready to be used by other Python code
# 
# Here is a visualization of this process:
# 
# <center>
# <img src="https://raw.githubusercontent.com/bradleyboehmke/uc-bana-6043/main/book/images/import-framework.png" alt="import-framework.png" width="80%" height="80%"/>
# </center>

# ## Delimited files
# 
# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_my7xrpxj&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_span5d75" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: Importing tabular data"></iframe>
# ```
# 
# Text files are a popular way to hold and exchange tabular data as almost any data application supports exporting data to the CSV (or other text file) format. Text file formats use delimiters to separate the different elements in a line, and each line of data is in its own line in the text file. Therefore, importing different kinds of text files can follow a fairly consistent process once you’ve identified the delimiter.
# 
# Although there are other approaches to importing delimited files, Pandas is often the preferred approach as it greatly simplifies the proess and imports the data directly into a DataFrame -- the data structure of choice for tabular data in Python.
# 
# The `read_csv` function is used to import a tabular data file, a CSV, into a DataFrame. The following will import a data set describing the sale of individual residential property in Ames, Iowa from 2006 to 2010 ([source](http://jse.amstat.org/v19n3/decock.pdf)).

# In[1]:


import pandas as pd

ames = pd.read_csv('../data/ames_raw.csv')


# We see that our imported data is represented as a DataFrame:

# In[2]:


type(ames)


# We can look at it in the Jupyter notebook, since Jupyter will display it in a well-organized, pretty way.

# In[3]:


ames


# This is a nice representation of the data, but we really do not need to display that many rows of the DataFrame in order to understand its structure. Instead, we can use the `head()` method of data frames to look at the first few rows. This is more manageable and gives us an overview of what the columns are. Note also the the missing data was populated with NaN.

# In[4]:


ames.head()


# ### File paths
# 
# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_qq3gp8gu&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_2ln4s8wa" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: File paths"></iframe>
# ```
# 
# It's important to understand where files exist on your computer and how to reference those paths. There are two main approaches:
# 
# 1. Absolute paths
# 2. Relative paths
# 
# An **absolute path** always contains the root elements and the complete list of directories to locate the specific file or folder. For the ames_raw.csv file, the absolute path on my computer is:

# In[5]:


import os

absolute_path = os.path.abspath('../data/ames_raw.csv')
absolute_path


# I can always use the absolute path in `pd.read_csv()`:

# In[6]:


ames = pd.read_csv(absolute_path)


# In contrast, a **relative path** is a path built starting from the current location. For example, say that I am operating in a directory called "Project A". If I'm working in "my_notebook.ipynb" and I have a "my_data.csv" file in that same directory:
# 
# ```bash
# # illustration of the directory layout
# Project A
# ├── my_notebook.ipynb
# └── my_data.csv
# ```
# 
# Then I can use this relative path to import this file: `pd.read_csv('my_data.csv')`. This just means to look for the 'my_data.csv' file relative to the current directory that I am in.
#  
# Often, people store data in a "data" directory. If this directory is a subdirectory within my Project A directory:
# 
# ```bash
# # illustration of the directory layout
# Project A
# ├── my_notebook.ipynb
# └── data
#     └── my_data.csv
# ```
# 
# Then I can use this relative path to import this file: `pd.read_csv('data/my_data.csv')`. This just means to look for the 'data' subdirectory relative to the current directory that I am in and then look for the 'my_data.csv' file.
# 
# Sometimes, the data directory may not be in the current directory. Sometimes a project directory will look the following where there is a subdirectory containing multiple notebooks and then another subdirectory containing data assets. If you are working in "notebook1.ipynb" within the notebooks subdirectory, you will need to tell Pandas to go up one directory relative to the notebook you are working in to the main Project A directory and then go down into the data directory.
# 
# ```bash
# # illustration of the directory layout
# Project A
# ├── notebooks
# │   ├── notebook1.ipynb
# │   ├── notebook2.ipynb
# │   └── notebook3.ipynb
# └── data
#     └── my_data.csv
# ```
# 
# I can do this by using dot-notation in my relative path specification - here I use '..' to imply "go up one directory relative to my current location": `pd.read_csv('../data/my_data.csv')`.

# Note that the path specified in `pd.read_csv()` does not need to be a local path. For example, the ames_raw.csv data is located online at https://raw.githubusercontent.com/bradleyboehmke/uc-bana-6043/main/book/data/ames_raw.csv. We can use `pd.read_csv()` to import directly from this location:
# 
# ```python
# url = 'https://raw.githubusercontent.com/bradleyboehmke/uc-bana-6043/main/book/data/ames_raw.csv'
# ames = pd.read_csv(url)
# ```

# ### Metadata
# 
# Once we've imported the data we can get some descriptive metadata about our DataFrame. For example, we can get the dimensions of our DataFrame. Here, we see that we have 2,930 rows and 82 columns.

# In[7]:


ames.shape


# We can also see what type of data each column is. For example, we see that the first three columns (Order, PID, MS SubClass) are integers, the fourth column (MS Zoning) is an object, and the fifth (Lot Frontage) is a float.

# In[8]:


ames.dtypes


# The following are the most common data types that appear frequently in DataFrames.
# 
# - **boolean** - only two possible values, True and False
# - **integer** - whole numbers without decimals
# - **float** - numbers with decimals
# - **object** - typically strings, but may contain any object
# - **datetime** - a specific date and time with nanosecond precision
# 
# ```{note}
# Booleans, integers, floats, and datetimes all use a particular amount of memory for each of their values. The memory is measured in bits. The number of bits used for each value is the number appended to the end of the data type name. For instance, integers can be either 8, 16, 32, or 64 bits while floats can be 16, 32, 64, or 128. A 128-bit float column will show up as float128.
# Technically a float128 is a different data type than a float64 but generally you will not have to worry about such a distinction as the operations between different float columns will be the same.
# ```
# 
# We can also use the `info()` method, which provides output similar to dtypes, but also shows the number of non-missing values
# in each column along with more info such as:
# 
# * Type of object (always a DataFrame)
# * The type of index and number of rows
# * The number of columns
# * The data types of each column and the number of non-missing (a.k.a non-null) 
# * The frequency count of all data types
# * The total memory usage

# In[9]:


ames.info()


# ### Attributes & methods
# 
# ```{admonition} Video 🎥:
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_phulmdop&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_sqbvypxe" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043: DataFrame attributes &amp; methods"></iframe>
# ```
# 
# We've seen that we can use the dot-notation to access functions in libraries (i.e. `pd.read_csv()`). We can use this same approach to access things inside of _objects_. What's an object? Basically, a variable that contains other data or functionality inside of it that is exposed to users. Consequently, our DataFrame item is an object.
# 
# In the above code, we saw that we can make different calls with our DataFrame such as `ames.shape` and `ames.head()`. An observant reader probably noticed the difference between the two -- one has parentheses and the other does not. 
# 
# An **attribute** inside an object is simply a variable that is unique to that object and a **method** is just a function inside an object that is unique to that object.
# 
# ```{tip}
# Variables inside an object are often called attributes and functions inside objects are called methods.
# 
# **attribute**: A variable associated with an object and is referenced by name using dotted expressions. For example, if an object `o` has an attribute `a` it would be referenced as `o.a`
# 
# **method**: A function associated with an object and is also referenced using dotted expressions but will include parentheses. For example, if an object `o` has a method `m` it would be called as `o.m()`
# ```
# 
# Earlier, we saw the attributes `shape` and `dtypes`. Another attribute is `columns`, which will list all column names in our DataFrame.

# In[10]:


ames.columns


# Similar to regular functions, methods are called with parentheses and often take arguments. For example, we can use the `tail()` method to see the last _n_ rows in our DataFrame:

# In[11]:


ames.tail(3)


# ```{note}
# We will be exposed to _many_ of the available DataFrame methods throughout this course!
# ```

# ### Knowledge check
# 
# ```{admonition} Questions:
# :class: attention
# 1. Check out the help documentation for `read_csv()` by executing `pd.read_csv?` in a code cell. What parameter in `read_csv()` allows us to specify values that represent missing values?
# 2. Read in this [energy_consumption.csv file](https://raw.githubusercontent.com/bradleyboehmke/uc-bana-6043/main/book/data/energy_consumption.csv).
# 3. What are the dimesions of this data? What information does the `size` attribute provide?
# 4. Check out the `describe()` method. What information does this provide?
# ```

# ## Excel files
# 
# With Excel still being the spreadsheet software of choice its important to be able to efficiently import and export data from these files. Often, many users will simply resort to exporting the Excel file as a CSV file and then import into Python using pandas.read_csv; however, this is far from efficient. This section will teach you how to eliminate the CSV step and to import data directly from Excel using pandas’ built-in `read_excel()` function.
# 
# To illustrate, we'll import so mock grocery store products data located in a products.xlsx file. 
# 
# ```{note}
# You may need to install the openpyxl dependency. You can do so with either of the following:
# 
# - pip install openpyxl
# - conda install openpyxl
# ```
# 
# To read in Excel data with pandas, you will use the `ExcelFile()` and `read_excel()` functions. ExcelFile allows you to read the names of the different worksheets in the Excel workbook. This allows you to identify the specific worksheet of interest and then specify that in `read_excel`.

# In[12]:


products_excel = pd.ExcelFile('../data/products.xlsx')
products_excel.sheet_names


# ```{warning}
# If you don't explicitly specify a sheet then the first worksheet will be imported.
# ```

# In[13]:


products = pd.read_excel('../data/products.xlsx', sheet_name='products data')
products.head()


# ## SQL databases
# 
# Many organizations continue to use relational databases along with SQL to interact with these data assets. Python has many tools to interact with these databases and you can even query SQL database tables with Panda's `read_sql` command. Pandas relies on a third-party library called [SQLAlechmy](https://www.sqlalchemy.org/) to establish a connection to a database.
# 
# To connect to a database, we need to pass a connection string to SQLAlechmy's `create_engine()` function. The general form of a connection string is the following: `dialect+driver://username:password@host:port/database`.
# 
# ```{note}
# Read more about [engine configuration here](https://docs.sqlalchemy.org/en/latest/core/engines.html).
# ```
# 
# In this example I will illustrate connecting to a local sqlite database. To do so the connection string looks like: `sqlite:///<path_to_db>`.  The following illustrates with the example [Chinook Database](https://www.sqlitetutorial.net/sqlite-sample-database/), which I've downloaded to my data directory.

# In[14]:


from sqlalchemy import create_engine

engine = create_engine('sqlite:///../data/chinook.db')


# Once I've made the connection, I can use `pd.read_sql()` to read in the "tracks" table directly as a Pandas DataFrame.

# In[15]:


tracks = pd.read_sql('tracks', con=engine)
tracks.head()


# If you are familiar with SQL then you can even pass a SQL query directly in the `pd.read_sql()` call. For example, the following SQL query:
# 
# 1. SELECTS the name, composer, and milliseconds columns,
# 2. FROM the tracks table,
# 3. WHERE observations in the milliseconds column are greater than 200,000 and WHERE observations in the composer column are not missing (NULL)

# In[16]:


sql_query = '''SELECT name, composer, milliseconds
               FROM tracks
               WHERE milliseconds > 200000 and composer is not null'''

long_tracks = pd.read_sql(sql_query, engine)
long_tracks.head()


# ## Many other file types
# 
# There are many other file types that you may encounter in your career. Most of which we can import into Python one way or another. Most tabular (2-dimensional data sets) can be imported directly with Pandas. For example, [this page](https://pandas.pydata.org/docs/search.html?q=read_) shows a list of the many `pandas.read_xxx()` functions that allow you to read various data file types.
# 
# While tabular data is the most popular in data science, other types of data will are used as well. These are not as important as the pandas DataFrame, but it is good to be exposed to them. These additional data formats are going to be more common in a fully functional programming language like Python.
# 
# ### JSON files
# 
# A common example is a [JSON](https://en.wikipedia.org/wiki/JSON) file -- these are non-tabular data files that are popular in data engineering due to their space efficiency and flexibility. Here is an example JSON file:
# 
# ```json
# {
#     "planeId": "1xc2345g",
#     "manufacturerDetails": {
#         "manufacturer": "Airbus",
#         "model": "A330",
#         "year": 1999
#     },
#     "airlineDetails": {
#         "currentAirline": "Southwest",
#         "previousAirlines": {
#             "1st": "Delta"
#         },
#         "lastPurchased": 2013
#     },
#     "numberOfFlights": 4654
# }
# ```
# 
# ```{note}
# Does this JSON data structure remind you of a Python data structure? The JSON file bears a striking resemblance to the Python `dict`ionary structure due to the key-value pairings.
# ```
# 
# JSON Files can be imported using the json library (from the Standard library) paired with the `with` statement and the `open()` function.
# 
# ```{type}
# This syntax is a little unique from what we've seen. We call the `with` statement a context manager. You can read more about context managers [here](https://book.pythontips.com/en/latest/context_managers.html).
# ```

# In[17]:


import json

with open('../data/json_example.json', 'r') as f:
    imported_json = json.load(f)


# We can then verify that our imported object is a `dict`:

# In[18]:


type(imported_json)


# And we can view the data:

# In[19]:


imported_json


# ### Pickle files
# 
# So far, we've seen that tabular data files can be imported and represented as DataFrames and JSON files can be imported and represented as dicts, but what about other, more complex data?
# 
# Python's native data files are known as **Pickle** files:
# 
# * All Pickle files have the `.pickle` extension
# * Pickle files are great for saving native Python data that can't easily be represented by other file types such as:
#    - pre-processed data,
#    - models,
#    - any other Python object...
# 
# Similar to JSON files, pickle files can be imported using the pickle library paired with the `with` statement and the `open()` function:

# In[20]:


import pickle

with open('../data/pickle_example.pickle', 'rb') as f:
    imported_pickle = pickle.load(f)


# We can view this file and see it's the same data as the JSON:

# In[21]:


imported_pickle


# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# 1. Python stores its data in _______ .
# 2. What happens to Python's data when the Python session is terminated?
# 3. Load the hearts.csv data file into Python using the pandas library.
# 4. What are the dimensions of this data? What data types are the variables in this data set?
# 5. Assess the first 10 rows of this data set.
# 6. Now import the hearts_data_dictionary.csv file, which provides some information on each variable. Do the data types of the hearts.csv variables align with the description of each variable?
# ```

# ## Computing environment

# In[22]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab,pandas,sqlalchemy')

