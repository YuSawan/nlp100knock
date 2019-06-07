#!/usr/bin/env python
# coding: utf-8

# In[3]:


def word_ngram(t,n):
    words = t.split()
    bi_list = []
    for i in range(len(words)-n+1):
        bi_list.append(words[i:i+n])
    return bi_list
    
def char_ngram(t,n):
    bi_list = []
    for i in range(len(t)-n+1):
        if t[i] == ' ' or t[i] == '.':
            continue
        bi_list.append(t[i:i+n])
    return bi_list
    
if __name__ in '__main__':
    t = input()
    print (word_ngram(t,2))
    print (char_ngram(t,2))


# 

# In[ ]:




