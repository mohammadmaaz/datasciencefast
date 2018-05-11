
# coding: utf-8

# In[40]:

import pandas as pd


# In[41]:

df = pd.read_csv('u.data',header=None,delimiter='\t',names = ['userId', 'movieId', 'rating','timestamp'])


# In[42]:

df.head(3)


# In[43]:

rating = df.loc[:,'rating']


# In[44]:

storerating = []


# In[45]:

for rate in rating:
    if rate <=3:
        storerating.append(0)
    else:
        storerating.append(1)


# In[46]:

len(storerating)


# In[47]:

x = 0
y = 0
for c in storerating:
    if(c == 0):
        x +=1
    else:
        y +=1


# In[48]:

print("Less than equal to 3 : %d",x)
print("Greater than equal to 3 : %d",y)


# In[49]:

sampleten = []


# In[50]:

storerating_len = len(storerating)


# In[51]:

storerating_len


# In[52]:

for i in range(0,storerating_len,10):
    sampleten.append(storerating[i])


# In[53]:

len(sampleten)


# In[54]:

10000/100000


# In[55]:

1/10


# In[56]:

x = 0
y = 0
for c in sampleten:
    if(c == 0):
        x +=1
    else:
        y +=1


# In[57]:

print("Sample of 10000 Less than equal to 3 : %d",x)
print("Sample of 10000 Greater than equal to 3 : %d",y)


# In[ ]:




# In[ ]:



