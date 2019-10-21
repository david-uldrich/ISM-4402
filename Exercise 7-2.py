#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import matplotlib.pyplot as plt
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,status,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Status','Grades'])

get_ipython().magic(u'matplotlib inline')
df = df.set_index(df['Status'])
df.plot(kind='bar')

