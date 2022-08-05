#!/usr/bin/env python
# coding: utf-8

# ### Prasad Rajesh Posture  
# **Batch**: June 2022  
# Data Analytics with Python

# **Task :** Peform data analysis on India's statewise covid-19 data using various visualization tools.

# #### `import` libraries

# In[1]:


import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")


# #### Loading the data

# Datasource : https://www.kaggle.com/datasets/prasadposture121/covid19-india-statewise-data

# In[2]:


data= pd.read_csv('Covid-19_India.csv')
data.head()


# #### Renaming the data columns

# In[3]:


data.rename(columns = {'Active Ratio':'Active Ratio (%)', 'Discharge Ratio': 'Discharge Ratio (%)', 'Death Ratio': 'Death Ratio (%)'}, inplace = True)


# ### Exploratory Data Analysis

# #### Various data types of the dataset

# In[4]:


data.dtypes


# #### Columns of the data

# In[5]:


data.columns


# #### Checking fot the null values

# In[6]:


data.isnull().sum()


# #### Checking for the duplicate values

# In[7]:


data.duplicated().sum()


# #### Shape of the dataset (rows, columns)

# In[8]:


data.shape


# #### Size of the dataset
# 

# In[9]:


data.size


# #### Basic Information of the dataset

# In[10]:


data.info()


# #### Stastical information of each column

# In[11]:


data.describe()


# #### See if there is any correlation between any data columns

# Numeric Correlations

# In[12]:


data.corr()


# Corrrelation using Heatmap

# In[13]:


plt.figure(figsize=(6,6))
sns.heatmap(data.corr())
plt.title("Correlation Between the Datacolumns")


# Correlation using Scatter Matrix

# In[14]:


scatter_matrix(data,figsize=[15,15],diagonal='kde')
plt.show()


# **Conclusion:** It is evident from these plots and the numerical data of correlation that the total number cases and number of discharged people show high positive correlation therefore lot of people are getting recovered from this disease. This is also supported by the negative correlation between death ratio and discharge ratio. Although there is a significant amount of correlation between number deaths and total cases it is because of the exponetial spread of the virus.

# ### Data Visualization

# #### Comparing each attribute of the dataset such as total number of cases, number of active cases, deaths etc with different states / union territories.

# In[15]:


#Getting the different attributes of the dataset
attributes=list(data.columns)
attributes.remove('State/UTs')
attributes


# In[16]:


for attribute in attributes:
    data=data.sort_values(attribute,ascending=False)
    plt.figure(figsize=(10,10))
    sns.barplot(x='State/UTs',y=attribute,palette='CMRmap',data=data)
    plt.title(attribute+" per State/UTs ",fontsize=15)
    plt.xticks(rotation=90)
    plt.show();


# **Conclusion:** Maharashtra has the highest number of total cases and Andman and Nicobar are at the last place. Kerala has the highest number of active cases. Number of discharged people is large in Maharashtra but number of deaths are large as well that is because of the large and dense population in the different cities of Maharashtra. Haryana has the highest active case ratio and Punjab has the highest death ratio but the discharge ratio is almost same for each and every state / union territory. Finally the last plot gives population of each state /  union territory.

# #### One can make this plot more interesting by comparing the attributes of states / union territories on the map of India.

# In[17]:


for attribute in attributes:
    fig=px.choropleth(data,
             geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
             featureidkey='properties.ST_NM',   
             locations='State/UTs',       
              color=attribute,
              color_continuous_scale='Inferno',
               title=attribute+' per State / UTs' ,  
               height=700
              )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.show()
#                                                                                               Scroll Down From Here >>>>>>>


# The above plots show same comparitive relationship between states/UTs and the attributes like the barplots, but with the map we can easily understand how the virus might have spread across the contry. The limitation of this plot is due smaller size union territories are not easily visible.

# #### Getting the total number of cases,number of active cases , number deaths and discharges across the nation

# In[18]:


data2=data.sum(axis=0)
data2[['Total Cases','Active','Discharged','Deaths']]


# The End
