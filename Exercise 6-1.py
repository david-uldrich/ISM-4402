#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df = df.sort_values(by=['lname','age','grade'], ascending=[True,True,True])
df.head()

