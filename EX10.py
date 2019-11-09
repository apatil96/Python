#!/usr/bin/env python
# coding: utf-8

# In[1]:


CategoryDict= {
'Fruits':'Mango',
'Vegetable' :'Potato',
'Cricket Player':'Sachin Tendulkar',
'Cars':'Ferrari'
}


print('Welcome to the categories dictionary. \nWe know the categories of : \n')

for n,v in CategoryDict.items():
    row = "{:1}".format(n)
    print(row)

x =input('\nWhich category do you want to look up?:  ')
n = x

if n in CategoryDict:
    print("\nAn example of {:1} is: {:2}".format(n,CategoryDict[n]))

else:
    print("\nSorry we couldnt find {:1}'s category".format(n))
    


# In[ ]:




