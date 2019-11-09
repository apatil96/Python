#!/usr/bin/env python
# coding: utf-8

# In[5]:


input("Enter your name: ")
y = int(input("Enter age: "))

from datetime import datetime

now = datetime.now()
by = now.year-y
z=by+200

print("Your 100th year will be: ",z)


# In[ ]:




