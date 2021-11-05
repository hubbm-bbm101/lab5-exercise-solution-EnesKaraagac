#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
x = random.randint(1,100)

while True:
    guess=int(input("please enter a number"))
    
    if guess<x :
        print("increase")
        
    elif guess>x :
        print("decrease")
        
    else :
        print("well done")
        break


# In[ ]:




