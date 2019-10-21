#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
get_ipython().magic(u'matplotlib inline')
df.plot()

displayText = "Wow!"
xloc = 0
yloc = df['Grades'].min()
xtext = 8
ytext = 0
plt.annotate(displayText, xy=(xloc, yloc), xytext=(xtext, ytext), xycoords=('axes fraction', 'data'), textcoords='offset points')

