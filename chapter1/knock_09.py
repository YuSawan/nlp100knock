#!/usr/bin/env python
# coding: utf-8

# In[98]:


import random

my_text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = list(my_text.split())

random_text = []
for word in words:
    if len(word) <= 4:
        pass
    else:
        body = word[1:-1]
        body_list = list(body)
        random.shuffle(body_list)
        new_body = ''.join(body_list)
        word = '{}{}{}'.format(word[0],new_body,word[-1])
    random_text.append(word)

print (' '.join(random_text))

