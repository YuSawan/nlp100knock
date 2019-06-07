#!/usr/bin/env python
# coding: utf-8

# In[4]:


t = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = list(i for i in t.split())
word_len = []
for word in words:
    if word.endswith(',') or word.endswith('.'):
        word = word[:-1]
    word_len.append(len(word))

print (word_len)

