#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

# Create the bin dividers
bins = [0,80,100]
# Create names for the four groups
group_names = ['Fail','Pass']

df['passfail'] = pd.cut(df['grade'], bins, labels=group_names)
df

