#!/usr/bin/env python
# coding: utf-8

# # TO PRINT ALL THE PRIME NUMBERS BETWEEN 1 TO 200 USINF FOR LOOP

# In[1]:


minimum=1


# In[2]:


maximum=200


# In[5]:


print("Prime numbers between", minimum , "and", maximum , "are:")


for num in range(1,200+1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
       


# # SUPPOSING YOU ALL ARE PILOTS YOU HAVE TO LAND A PLANE , THE ALTITUDE REQUIRED FOR LANDIND PLANE IS 1000ft. IF IT IS MORE THAN 1000ft. but less than 5000ft. then land down to 1000ft. IF THE ALTITUDE IS HIGHER THAN 5000ft. THEN TURN AROUND AND TRY LATER
# 

# In[ ]:


#altitude i in ft
i="altitude"

for i in range(0,1000):
     i=int(input("Tell the altitude= "))
     print("safe to land")


     for i in range(1001,5000):
            if i>1000 :
                i=int(input("Tell the altitude= "))
                print("Bring plane down to 1000ft")
                
                
            else:
                print("Turn around try later")
    

