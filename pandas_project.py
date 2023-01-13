#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


np.random.seed(20)
df = pd.DataFrame(np.random.rand(1000,1) , index=pd.date_range('2021-07-18' , periods=1000), columns=['data'])


# In[3]:


df


# In[4]:


df.plot()


# In[5]:


df.data.cumsum()


# In[6]:


df.data.cumsum().plot()


# In[7]:


df


# In[9]:


df['data1']=df.data.cumsum()
df['data2']=df.['data'].apply[lambda x:x*3]


# In[10]:


df


# In[13]:


df['data1']=df.data.cumsum()
df['data2'] = df['data'].apply(lambda x : x *3)


# In[11]:


df


# In[14]:


df


# In[15]:


df.plot()


# In[16]:


df1=sns.load_dataset('iris')


# In[17]:


df1


# In[18]:


df1=sns.load_dataset('iris')


# In[19]:


df1


# In[23]:


df1.plot(figsize=(10,10)),title=("dataplot"))


# In[22]:


df1.plot(figsize=(10,10)),title=("dataplot"))


# In[24]:


df1.plot()


# In[28]:


gf=df1.plot(figsize=(10,10),title="isrish data")
gf.set_xlabel("this is my x axis")
gf.set_ylabel("this is my y axis")


# In[27]:


gf.set_xlabel("this is my x axis")
gf.set_ylabel("this is my y axis")
gf.plot()


# In[29]:


df1


# In[33]:


df1.iloc[0][0:3].plot(kind='bar')


# In[37]:


df2=sns.load_dataset('titanic')


# In[38]:


df2


# In[39]:


df2[0]


# In[41]:


df2['pclass'].plot(kind='bar')


# In[43]:


pd.DataFrame(np.random.rand(10,4), columns =['a' , 'b' , 'c', 'd'])


# In[44]:


df3=pd.DataFrame(np.random.rand(10,4), columns =['a' , 'b' , 'c', 'd'])


# In[45]:


df3


# In[46]:


df3.plot.bar()


# In[47]:


df1.plot.hist()


# In[49]:


df1['sepal_width'].plot.hist()


# In[51]:


df1.hist(figsize=(10,10) , color="blue")


# In[52]:


df1.plot.scatter(x='sepal_length', y='petal_width')


# In[54]:


df1.plot.hexbin(x='sepal_length', y='petal_width' , label='amalesh' , gridsize=10)


# In[55]:


df


# In[57]:


d=df.iloc[0]


# In[58]:


d.plot.pie()


# In[59]:


df1


# In[65]:


a=df1.head().T


# In[70]:


a.iloc[0:4].plot.pie(subplots=True)


# In[71]:


df1


# In[74]:


pd.plotting.scatter_matrix(df1 ,figsize=(10,10) , diagonal='kde')


# In[75]:


df


# In[78]:


df['data'].plot()


# In[80]:


get_ipython().system('pip install plotty')
get_ipython().system('pip install cufflinks')


# In[81]:


get_ipython().system('pip install plotly')
get_ipython().system('pip install cufflinks')


# In[82]:


from plotly.offline import iplot
import plotly as py 
import plotly.tools as tls 
import cufflinks as cf


# In[83]:


py.offline.init_notebook_mode(connected=True)
cf.go_offline()


# In[84]:


df1


# In[85]:


df1.iplot()


# In[88]:


df2.iplot( x= 'fare' , y= 'age')


# In[90]:


cf.getheme()


# In[ ]:




