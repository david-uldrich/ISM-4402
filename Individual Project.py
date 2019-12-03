#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import matplotlib.pyplot as plt

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()

get_ipython().magic(u'matplotlib inline')


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[6]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:


df['Years Experience'].mean()


# In[8]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[9]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[43]:


df.hist(column="Cars Sold", by='Gender')


# In[44]:


df.boxplot(column="Hours Worked", by='Gender')

