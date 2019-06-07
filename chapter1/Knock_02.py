#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = 'パトカー'
b = 'タクシー'
s = []

for i in range(len(a)):
    s += a[i]
    s += b[i]
    
print (*s,sep=(''))


# In[ ]:




