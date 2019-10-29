#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

plt.scatter(df.index, df['hours'])

plt.scatter(df.index, df['grade'])

