#!/usr/bin/env python
# coding: utf-8

# In[8]:


x=int(input("Enter the degrees in Fahrenheit "))
def convert(y):
    def sbtract(z):
        z=z-32
        return z
    def multiply(a):
        a=a*5/9.0000
        return a
    print("It's %f degrees" % multiply(sbtract(y)))
convert(x)


# In[ ]:




