#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
names = ['Nike','Adidas','New Balance','Puma','Reebok']
prices = [176,59,47,38,99]
PriceList = zip(names,prices)
df = pd.DataFrame(data = PriceList, columns=['Names','Prices'])

writer = pd.ExcelWriter('dataframe.xlsx','xlsxwriter')
df.to_excel(writer, sheet_name='Sheet 1')
writer.save()

