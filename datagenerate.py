# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:57:46 2020

@author: DELL
"""
import numpy as  np
import pandas as pd
a=[]
b=[]
c=[]
for i in range(0,100):
    a.append(np.random.randint(0,100))
    b.append(np.random.randint(0,100))
    c.append(np.random.randint(0,100))
family_1=pd.DataFrame({"A":a,"B":b,"C":c})
x=abs(np.random.rand(100)*100)
y=abs(np.random.rand(100)*100)
z=abs(np.random.rand(100)*100)
family_2=pd.DataFrame({"A":x,"B":y,"C":z})
family_1.to_csv("Family_1.csv")
family_2.to_csv("Family_2.csv")
