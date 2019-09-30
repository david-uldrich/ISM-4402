#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

import numpy as np
df['timemgmt'] = np.where((df['exercise']>3) & (df['hours']>17),'busy','')
df

