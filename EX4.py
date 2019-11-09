#!/usr/bin/env python
# coding: utf-8

# In[8]:


FBinfo= {
1: {'UserName':'GauravGhase','num_of_frnds':1002,'Place':'Kholapur','Date_Of_Birth':'05/04/1996','DOAC':'08/09/2007'},
2: {'UserName':'Gkalidin','num_of_frnds':100,'Place':'Khol','Date_Of_Birth':'05/04/1997','DOAC':'08/09/2007'},
3: {'UserName':'Yash123','num_of_frnds':102,'Place':'pur','Date_Of_Birth':'01/03/1996','DOAC':'08/09/2007'},
4: {'UserName':'ammu','num_of_frnds':1023,'Place':'Khour','Date_Of_Birth':'07/04/1996','DOAC':'08/09/2007'},
5: {'UserName':'Parshya','num_of_frnds':1222,'Place':'holapur','Date_Of_Birth':'09/04/1996','DOAC':'08/09/2007'},
6: {'UserName':'Umya','num_of_frnds':1,'Place':'latur','Date_Of_Birth':'05/04/1956','DOAC':'08/09/2007'},
7: {'UserName':'Nenu','num_of_frnds':10,'Place':'shapur','Date_Of_Birth':'05/04/1986','DOAC':'08/09/2007'},
8: {'UserName':'Pinku','num_of_frnds':100,'Place':'anur','Date_Of_Birth':'05/04/1936','DOAC':'08/09/2007'},
9: {'UserName':'Omii','num_of_frnds':10023,'Place':'Khopur','Date_Of_Birth':'05/04/1995','DOAC':'08/09/2007'},
10: {'UserName':'Parshu','num_of_frnds':100245,'Place':'Tholapur','Date_Of_Birth':'05/04/1994','DOAC':'08/09/2007'},
11: {'UserName':'Grishma','num_of_frnds':10002,'Place':'Kholapur','Date_Of_Birth':'05/04/196','DOAC':'08/09/2007'},
12: {'UserName':'AmitPatil','num_of_frnds':10,'Place':'puri','Date_Of_Birth':'05/04/1796','DOAC':'08/09/2007'},
13: {'UserName':'Rajesh','num_of_frnds':256,'Place':'Kholi','Date_Of_Birth':'05/04/1906','DOAC':'08/09/2007'},
14: {'UserName':'Sheela','num_of_frnds':3768,'Place':'Khr','Date_Of_Birth':'05/04/1990','DOAC':'08/09/2007'},
15: {'UserName':'Anusha','num_of_frnds':1093,'Place':'Kpur','Date_Of_Birth':'05/04/1986','DOAC':'08/09/2007'},
}



print("Sr.No    UserName         DOA")
print("************************************")

for people,values in FBinfo.items():
    row = "{:2}       {:13}   {:5}".format(people,
            values['UserName'],
            values['DOAC'])
    print(row)
print("*************************************")


# In[ ]:


def dec_fun(fun):
    def wrap_fun(*args, **kwargs):
        x = input('Your First name: ')
        y = input('Your Last name: ')
        a = x[0:2]
        b = y[0:2]
        print('Your email is {:2}{:2}@example.com'.format(a,b))
        fun(*args, **kwargs)
        return fun
    return wrap_fun	

@dec_fun
def email_fun(*args, **kwargs):
    
    return email_fun

email_fun()


# In[ ]:


def reverse(s): 
    s = s[::-1] 
    return s
def dec_func(x,y,z):
    print(reverse(x))
    print(reverse(y))
    print(reverse(z))
a=input("enter first string")
b=a=input("enter first string")
c=a=input("enter first string")

    
    

