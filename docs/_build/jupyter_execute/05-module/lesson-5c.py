#!/usr/bin/env python
# coding: utf-8

# # Lesson 5c: Plotting with Bokeh
# 
# In the previous two lessons you learned how to use Panda's higher level plotting API for quick and simple visualization purposes and Matplotlib for lower level, detailed plotting capabilities. In this lesson you're going to learn about [Bokeh](https://bokeh.pydata.org/), which is a Python library for creating interactive visualizations for modern web browsers.
# 
# Bokeh helps you build beautiful graphics, ranging from simple plots to complex dashboards with streaming datasets. With Bokeh, you can create JavaScript-powered visualizations without writing any JavaScript yourself. This can be extremely useful for both exploratory data analysis and also refined beautiful visualization outputs and dashboards for stakeholders.
#  
# Although Bokeh is considered a lower level visualization API, generating plots with Bokeh is still fairly straightforward and intuitive. Bokeh makes it easy to create plots but also allows you a lot of flexibility to make your plots very complex, refined, and interactive.
# 
# In this lesson I'll teach the basics of Bokeh but provide you with resources where you can dig into more advanced Bokeh capabilities.
# 
# ```{note}
# Work through this lesson to create your first Bokeh plot and then at the end of this lesson is a longer video tutorial that will expose you to many other types of Bokeh plots that you can create.
# ```

# ## Prerequisites
# 
# Most of the functionality of Bokeh is accessed through submodules such as `bokeh.plotting` and `bokeh.models`. Also, when using Bokeh in a notebook we need to run `bokeh.io.output_notebook()` to make our plots viewable and interactive.

# In[1]:


import pandas as pd

# Our main plotting package (must have explicit import of submodules)
import bokeh.io
import bokeh.models
import bokeh.plotting
import bokeh.transform

# Enable viewing Bokeh plots in the notebook
bokeh.io.output_notebook()


# We'll use a cleaned up version of the Ames, IA housing data for illustration purposes:

# In[2]:


df = pd.read_csv('../data/ames_clean.csv')
df.head()


# ## Bokeh's grammar and our first plot with Bokeh
# 
# Constructing a plot with Bokeh consists of four main steps.
# 
# 1. Creating a figure on which to populate **glyphs** (symbols that represent data, e.g., dots for a scatter plot). Think of this figure as a "canvas" which sets the space on which you will "paint" your glyphs.
# 2. Defining a data source that is the reference used to place the glyphs.
# 3. Choose the kind of glyph you would like.
# 4. Refining the plot by adding titles, formatted axis labels, or even interactive components.
# 
# After completing these steps, you need to render the graphic.
# 
# Let's go through these steps to generate an interactive scatter plot of home sales price and total living area. So you have the concrete example in mind, the final graphic will look like this:

# In[3]:


# Create the figure, stored in variable `p`
p = bokeh.plotting.figure(
    frame_width=700,
    frame_height=350,
    title='Relationship between home sale price and living area \nAmes, Iowa (2006-2010)',
    x_axis_label='Living Area (Square feet)',
    y_axis_label='Sale Price'
)

source = bokeh.models.ColumnDataSource(df)

p.circle(
    source=source,
    x='GrLivArea',
    y='SalePrice',
    alpha=0.25
)

p.yaxis.formatter = bokeh.models.NumeralTickFormatter(format="$,")
p.xaxis.formatter = bokeh.models.NumeralTickFormatter(format=",")

tooltips = [("Sale Price","@SalePrice"),("SqFt","@GrLivArea")]
hover = bokeh.models.HoverTool(tooltips=tooltips, mode='mouse')
p.add_tools(hover)

bokeh.io.show(p)


# 1\. Our first step is creating a figure, our "canvas." In creating the figure, we are implicitly thinking about what kind of representation for our data we want. That is, we have to specify axes and their labels. We might also want to specify the title of the figure, whether or not to have grid lines, and all sorts of other customizations. Naturally, we also want to specify the size of the figure.
# 
# (Almost) all of this is accomplished in Bokeh by making a call to `bokeh.plotting.figure()` with the appropriate keyword arguments.

# In[4]:


# Create the figure, stored in variable `p`
p = bokeh.plotting.figure(
    frame_width=700,
    frame_height=350,
    title='Relationship between home sale price and living area \nAmes, Iowa (2006-2010)',
    x_axis_label='Living Area (Square feet)',
    y_axis_label='Sale Price'
)


# There are many more keyword attributes you can assign, including [all of those listed in the Bokeh Plot class](https://bokeh.pydata.org/en/latest/docs/reference/models/plots.html#bokeh.models.plots.Plot) and [the additional ones listed in the Bokeh Figure class](https://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.figure.Figure).
# 
# 2\. Now that we have set up our canvas, we can decide on the data source. It is convenient to create a **ColumnDataSource**, a special Bokeh object that holds data to be displayed in a plot. (We will later see that we can change the data in a ColumnDataSource and the plot will automatically update!) Conveniently, we can instantiate a ColumnDataSource directly from a Pandas data frame.

# In[5]:


source = bokeh.models.ColumnDataSource(df)


# ```{note}
# We could also instantiate a data source using a dictionary of arrays, like
# 
#     source = bokeh.models.ColumnDataSource(dict(x=[1, 2, 3, 4], y=[1, 4, 9, 16]))
# ```
# 
# 3\. We will choose dots (or circles) as our glyph. This kind of glyph requires that we specify  which column of the data source will serve to place the glyphs along the $x$-axis and which will serve to place the glyphs along the $y$-axis. We choose the `'GrLivArea'` column to specify the $x$-coordinate of the glyph and the `'SaledPrice'` column to specify the $y$-coordinate. Since there are a lot of observations clustered together we can control overplotting by adjusting the transparency with `alpha`.
# 
# We accomplish step 3 by calling one of the [**glyph methods**](https://docs.bokeh.org/en/latest/docs/user_guide/plotting.html#scatter-markers) of the Bokeh `Figure` instance, `p`. Since we are choosing dots, the appropriate method is `p.circle()`, and we use the `source`, `x`, and `y` kwargs to specify the positions of the glyphs.

# In[6]:


p.circle(
    source=source,
    x='GrLivArea',
    y='SalePrice',
    alpha=0.25
);


# 4\. Lastly, we can refine the plot in various ways. In this example we make the x and y-axis labels comma and dollar formatted respectively. We can also add [interactive components](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html#userguide-interaction) to our visuals. Here, I add a hover tool so that sale price and total living area is displayed when my mouse hovers over a point. 
# 
# ```{tip}
# We can specify these features (axis configuration and tooltips) when we instantiate the figure or afterwards by assigning attribute values to an already instantiated figure. 
# ```
# 
# The syntax for a tooltip is a list of 2-tuples, where each tuple represents the tooltip you want. The first entry in the tuple is the label and the second is the column from the data source that has the values. The second entry must be preceded with an `@` symbol signifying that it is a field in the data source and not field that is intrinsic to the plot, which is preceded with a `$` sign. If there are spaces in the column heading, enclose the column name in braces (i.e. `{name with spaces}`). (See the [documentation for tooltip specification](https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html#basic-tooltips) for more information.)

# In[7]:


p.yaxis.formatter = bokeh.models.NumeralTickFormatter(format="$,")
p.xaxis.formatter = bokeh.models.NumeralTickFormatter(format=",")

tooltips = [("Sale Price","@SalePrice"),("SqFt","@GrLivArea")]
hover = bokeh.models.HoverTool(tooltips=tooltips, mode='mouse')
p.add_tools(hover)


# Now that we have built the plot, we can render it in the notebook using `bokeh.io.show()`.

# In[8]:


bokeh.io.show(p)


# In looking at the plot, notice a toolbar to right of the plot that enables you to zoom and pan within the plot.

# ## The importance of tidy data frames
# 
# It might be clear for you now that building a plot in this way requires that the data frame you use be [tidy](l18_split_apply_combine.ipynb). The organization of tidy data is really what enables this and high level plotting functionality. There is a well-specified organization of the data.

# ## Code style in plot specifications
# 
# Specifications of plots often involves calls to functions with lots of keyword arguments to specify the plot, and this can get unwieldy without a clear style. You can develop your own style, maybe reading [Trey Hunner's blog post again](http://treyhunner.com/2017/07/craft-your-python-like-poetry/). I like to do the following.
# 
# 1. Put the function call, like `p.circle(` or `p = bokeh.plotting.figure(` on the first line.
# 2. The closed parenthesis for the function call is on its own line, unindented.
# 3. Any arguments are given as kwargs (even if they can also be specified as positional arguments) at one level of indentation.
# 
# Note that you *cannot* use method chaining when instantiating figures or populating glyphs.
# 
# If you adhere to a style (which is roughly the style imposed by [Black](https://black.readthedocs.io/en/stable/)), it makes your code cleaner and easier to read.

# ## Coloring with other dimensions
# 
# Let's say we wanted to make the same plot, but we wanted to color the points based on another feature such as whether the home has central air or not (`CentralAir`). To do this, we take advantage of two features of Bokeh.
# 
# 1. We create a color mapping using `factor_cmap()` that assigns colors to the discrete levels of a given factor (CentralAir in this example). Here, we simply assign red and blue colors; however, Bokeh has many [color palettes to choose from](https://docs.bokeh.org/en/latest/docs/reference/palettes.html).
# 2. We can then use the `scatter` method to assign the glyph of choice and pass the `color_mapper` object to `fill_color` and/or `fill_line`. I also add the legend field so it shows up in the plot and we can format our legend as necessary (i.e. add title, change font).

# In[9]:


# Create the figure, stored in variable `p`
p = bokeh.plotting.figure(
    frame_width=700,
    frame_height=350,
    title='Relationship between home sale price and living area \nAmes, Iowa (2006-2010)',
    x_axis_label='Living Area (Square feet)',
    y_axis_label='Sale Price'
)

source = bokeh.models.ColumnDataSource(df)

# create color mapper
color_mapper = bokeh.transform.factor_cmap(
    'CentralAir', 
    palette=['red', 'blue'], 
    factors=df['CentralAir'].unique()
    )
     
p.scatter(
    source=source,
    x='GrLivArea',
    y='SalePrice',
    marker='circle',
    alpha=0.25,
    fill_color=color_mapper,
    line_color=color_mapper,
    legend_field='CentralAir'
)

p.legend.title = "Has central air"

p.yaxis.formatter = bokeh.models.NumeralTickFormatter(format="$,")
p.xaxis.formatter = bokeh.models.NumeralTickFormatter(format=",")

tooltips = [("Sale Price","@SalePrice"),("SqFt","@GrLivArea")]
hover = bokeh.models.HoverTool(tooltips=tooltips, mode='mouse')
p.add_tools(hover)

bokeh.io.show(p)


# ## Saving Bokeh plots
# 
# After you create your plot, you can save it to a variety of formats. Most commonly you would save them as PNG (for presentations), SVG (for publications in the paper of the past), and HTML (for the paper of the future or sharing with colleagues). 
# 
# To save as a PNG for quick use, you can click the disk icon in the tool bar. 
# 
# To save to SVG, you first change the output backend to `'svg'` and then you can click the disk icon again, and you will get an SVG rendering of the plot. After saving the SVG, you should change the output backend back to `'canvas'` because it has much better in-browser performance.

# In[10]:


p.output_backend = 'svg'

bokeh.io.show(p)


# Now, click the disk icon in the plot above to save it.
# 
# After saving, we should switch back to canvas.

# In[11]:


p.output_backend = 'canvas'


# You can also save the figure programmatically using the `bokeh.io.export_svgs()` function. This requires additional installations, so we will not do it here, but show the code to do it. Again, this will only work if the output backed is `'svg'`.
# 
# ```python
# p.output_backend = 'svg'
# bokeh.io.export_svgs(p, filename='ames_sale_price_vs_living_area.svg')
# p.output_backend = 'canvas'
# ```
# 
# Finally, to save as HTML, you can use the `bokeh.io.save()` function. This saves your plot as a standalone HTML page. Note that the `title` kwarg is not the title of the plot, but the title of the web page that will appear on your Browser tab.

# In[12]:


bokeh.io.save(
    p, 
    filename='ames_sale_price_vs_living_area.html', 
    title='Bokeh plot'
);


# ```{note}
# You can ignore the warning. The resulting HTML page has all of the interactivity of the plot and you can, for example, email it to your collaborators for them to explore.
# ```

# ## Video Tutorial
# 
# ```{admonition} Video 🎥:
# The following video provides an overview of Bokeh and will also expose you to other types of plots you can create (i.e. line charts, histograms, area plots).
# 
# <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1492301/sp/149230100/embedIframeJs/uiconf_id/49148882/partner_id/1492301?iframeembed=true&playerId=kaltura_player&entry_id=1_ke04lf4v&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[forceMobileHTML5]=true&amp;flashvars[scrubber.sliderPreview]=false&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_f4zknbu7" width="640" height="610" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="BANA 6043 | Python Bokeh Tutorial | Python Data Visualization With Bokeh | Python Bokeh Dashboard | SimpliCode"></iframe>
# ```

# ## Exercises
# 
# ```{admonition} Questions:
# :class: attention
# 1. Spend some time going through the [Bokeh documentation and tutorials](https://docs.bokeh.org/en/latest/index.html). 
# 2. Pick a feature from the Ames Housing data and create a bar chart. Can you make a similar bar chart as we did in the Matplotlib tutorial?
# 3. Pick two continuous features from the Ames Housing data and create a scatter plot. Can you make a similar scatter plot as we did in the Matplotlib tutorial but with interactive components?
# 4. Now identify a categorical feature that you can color the above scatter plot by (i.e. `CentralAir`).
# 5. Using the hover tooltips, are you able to identify outliers in your plot(s)?
# ```

# ## Computing environment

# In[13]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p pandas,bokeh,jupyterlab')

