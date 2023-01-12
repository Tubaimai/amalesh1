#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


np.random.seed(20)
df = pd.DataFrame(np.random.rand(10,1) , index=pd.date_range('2021-07-18' , periods=10), columns=['data'])


# In[4]:


df


# In[5]:


df.plot()


# In[6]:


df.data.cumsum().plot()


# In[7]:


df.plot.bar()


# In[8]:


df.plot.barh()


# In[9]:


df.plot.hist()


# In[10]:


df1=pd.read_excel("bastudents.xlsx")
print(df1)


# In[11]:


df1.plot.scatter(x='Attendance' , y='Marks')


# In[12]:


df1.plot.hist()


# In[14]:


df1.plot.hexbin(x='Attendance' , y='Marks')


# In[15]:


df1.plot.hexbin(x='Attendance' , y='Marks',gridsize = 10)


# In[18]:


df1.plot.pie(subplots = True)


# In[ ]:




