#!/usr/bin/env python
# coding: utf-8

# In[2]:


def main(x,y,z):
    t = '{}時の{}は{}'.format(x,y,z)
    return t

if __name__ in '__main__':
    x = 12
    y = '気温'
    z = 22.4
    print(main(x,y,z))

