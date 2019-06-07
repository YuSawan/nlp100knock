#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys

def cipher(t):
    new_text = ''
    for char in t:
        if char.islower():
            char = chr(219-ord(char))
        new_text += char
    return new_text
    
if __name__ in '__main__':
    my_text = input()
    print (cipher(my_text))
    

