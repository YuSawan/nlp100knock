#!/usr/bin/env python
# coding: utf-8

# In[15]:


import argparse

def main(my_text):
    rows = sum(1 for row in open(my_text))
    return rows
    
if __name__ == '__main__':
    # Make a perser
    parser = argparse.ArgumentParser()
    # add argument to parser
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    # parse a argument
    args = parser.parse_args(args=[])
    
    print (main(args.train))


# In[ ]:




