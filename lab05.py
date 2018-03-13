
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df = pd.read_csv('u.data',header=None,delimiter='\t')


# In[3]:

print(df.head())


# In[4]:

#Second Column is for rating


# In[5]:

rating = df.loc[:,2]


# In[6]:

rating[0]


# In[7]:

df.info()


# In[8]:

len(rating)


# In[9]:

storerating = []


# In[10]:

for rate in rating:
    if rate <=3:
        storerating.append(0)
    else:
        storerating.append(1)


# In[11]:

len(storerating)


# In[12]:

storerating[0]


# In[ ]:



