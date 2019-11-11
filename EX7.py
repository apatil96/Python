#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
from os import listdir
import time
import datetime


print('FileName                   Size           Modification time')
print('*****************************************************************')

for x in listdir('.'):
        row = "{:20}  {:10}        {:20}".format(x,os.path.getsize(x),time.ctime(os.path.getmtime(x)))
        print(row)
print("*****************************************************************")
    


# In[ ]:




