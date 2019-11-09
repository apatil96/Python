#!/usr/bin/env python
# coding: utf-8

# In[ ]:


FBinfo= {
1: {'UserName':'GauravGhase','num_of_frnds':1002,'Place':'Kholapur','Date_Of_Birth':'05/04/1996','DOA':'08/09/2007'},
2: {'UserName':'Gkalidin','num_of_frnds':100,'Place':'Khol','Date_Of_Birth':'05/04/1997','DOA':'08/09/2007'},
3: {'UserName':'Yash123','num_of_frnds':102,'Place':'pur','Date_Of_Birth':'01/03/1996','DOA':'08/09/2007'},
4: {'UserName':'ammu','num_of_frnds':1023,'Place':'Khour','Date_Of_Birth':'07/04/1996','DOA':'08/09/2007'},
5: {'UserName':'Parshya','num_of_frnds':1222,'Place':'holapur','Date_Of_Birth':'09/04/1996','DOA':'08/09/2007'},
6: {'UserName':'Umya','num_of_frnds':1,'Place':'latur','Date_Of_Birth':'05/04/1956','DOA':'08/09/2007'},
7: {'UserName':'Nenu','num_of_frnds':10,'Place':'shapur','Date_Of_Birth':'05/04/1986','DOA':'08/09/2007'},
8: {'UserName':'Pinku','num_of_frnds':100,'Place':'anur','Date_Of_Birth':'05/04/1936','DOA':'08/09/2007'},
9: {'UserName':'Omii','num_of_frnds':10023,'Place':'Khopur','Date_Of_Birth':'05/04/1995','DOA':'08/09/2007'},
10:{'UserName':'Parshu','num_of_frnds':100245,'Place':'Tholapur','Date_Of_Birth':'05/04/1994','DOA':'08/09/2007'},
11:{'UserName':'Grishma','num_of_frnds':10002,'Place':'Kholapur','Date_Of_Birth':'05/04/196','DOA':'08/09/2007'},
12:{'UserName':'AmitPatil','num_of_frnds':10,'Place':'puri','Date_Of_Birth':'05/04/1796','DOA':'08/09/2007'},
13:{'UserName':'Rajesh','num_of_frnds':256,'Place':'Kholi','Date_Of_Birth':'05/04/1906','DOA':'08/09/2007'},
14:{'UserName':'Sheela','num_of_frnds':3768,'Place':'Khr','Date_Of_Birth':'05/04/1990','DOA':'08/09/2007'},
15:{'UserName':'Anusha','num_of_frnds':1093,'Place':'Kpur','Date_Of_Birth':'05/04/1986','DOA':'08/09/2007'},
}


for number,values in FBinfo.items():
    
    x = input("Enter a number from 1-15 you want to access record:  ")
    x = number

    if number in FBinfo:
        print("The record is: {:1}   {:1}     {:1}    {:1}     {:1} ".format(values['UserName'],values['num_of_frnds'],values['Place'],values['Date_Of_Birth'],values['DOA']))
    else:
        print('You have entered an invalid number')


# In[ ]:




