#!/usr/bin/env python
# coding: utf-8

# In[1]:


def dec_func(func):
    def wrapper(*args, **kwargs):
        a=(input("Enter first string "))
        b=(input("Enter second string "))
        c=(input("Enter third string "))
        func(*args, **kwargs)
        print("\nThe reverse order of the strings are: ",c," ",b," ",a)
        return(func)
    return wrapper
@dec_func
def rev(*args, **kwargs):
    return rev
rev()


# In[ ]:





# In[ ]:




