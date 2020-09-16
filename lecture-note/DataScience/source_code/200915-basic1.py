#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


get_ipython().system('pip install xlrd')


# In[3]:


df = pd.read_excel("../data/02. sales-funnel.xlsx")
df.head()


# In[4]:


pd.pivot_table(df,index=["Name"])


# In[5]:


pd.pivot_table(df,index=["Manager","Rep"])


# In[6]:


pd.pivot_table(df,index=["Manager","Rep"],values=["Price"])


# In[7]:


pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],aggfunc=np.sum)


# In[ ]:




