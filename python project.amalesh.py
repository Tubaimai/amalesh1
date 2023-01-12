#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
df=pd.read_excel('Student Survey.xlsx')
df


# In[48]:


df.Age > 12


# In[16]:


df[df.Age > 12]


# In[17]:


df[df.Age==15]


# In[27]:


df1=df[df.Exchange=='Card']


# In[30]:


df[((df.Exchange=='Card')&(df.Age.max()))]


# In[32]:


df.Age.sort_values()


# In[38]:


df.sort_values('Gadgets', inplace=True)


# In[39]:


df


# In[42]:


df3=df[df['Total Amount of Purchases'] > 321.67]


# In[44]:


df3


# In[43]:


df3.iloc[0:5]


# In[45]:


df3.describe()


# In[ ]:




