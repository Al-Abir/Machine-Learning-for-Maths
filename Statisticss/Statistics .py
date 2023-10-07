#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np


# In[13]:


df = pd.read_csv("income.csv", names=["name","income"], skiprows=[0])
df


# In[14]:


df.describe() 


# In[15]:


df.income.quantile(0)


# In[16]:


df.income.quantile(0.25,interpolation="higher")         


# In[17]:


df.income.quantile(0.5,interpolation="higher")


# In[18]:


df.income.quantile(0.75)


# In[19]:


percentile_99 = df.income.quantile(0.99)
percentile_99


# In[20]:


df[df.income>percentile_99]


# In[21]:


df.income.mean()


# In[22]:


df_new = df.fillna(df.income.mean())
df_new


# In[23]:


df_new = df.fillna(df.income.median())
df_new


# In[ ]:




