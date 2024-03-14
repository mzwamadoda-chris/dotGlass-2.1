#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("C:\\Users\somel\\Downloads\\Dots Potential Customer Survey Data - Sheet1.csv")


# In[3]:


df


# In[4]:


df.shape




# In[5]:


df.info()




# In[6]:


df.describe()




# In[7]:


df.isnull().sum()



# In[7]:


from sklearn.preprocessing import LabelEncoder


# In[8]:


label_encoder = LabelEncoder()
df['Education Status'] = label_encoder.fit_transform(df['Education Status'])


# In[9]:


df = pd.get_dummies(df, columns = ['Country', 'Gender'])


# In[10]:


correlation_matrix =df.corr()
correlation_matrix



# In[ ]:




