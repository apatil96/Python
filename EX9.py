#!/usr/bin/env python
# coding: utf-8

# In[2]:


def replaceOdd(oldString):
    newString=" "
    for i in range(len(oldString)):
        if i % 2 == 0:
            newString = newString + oldString[i]
    return newString

x=input("Enter a String : ")
replaceOdd(x)


# In[ ]:




