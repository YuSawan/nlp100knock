#!/usr/bin/env python
# coding: utf-8

# In[3]:


import knock_05

a = "paraparaparadise"
b = "paragraph"

X = set(knock_05.char_ngram(a,2))
Y = set(knock_05.char_ngram(b,2))

print ("和集合 {}".format(X|Y))
print ("積集合 {}".format(X&Y))
print ("差集合 a-b {}".format(X-Y))
print ("差集合 b-a {}".format(Y-X))

if 'se' in X:
    print ('a is included se')
else:
    print ('a is not included se')
if 'se' in Y:
    print ('b is included se')
else:
    print ('b is not included se')    


# In[ ]:




