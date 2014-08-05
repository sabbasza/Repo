# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 11:58:03 2014

@author: Shiva
"""

minIdx=1;
maxIdx=1001;
for i in range(minIdx,maxIdx):
    isPrime=True;
    for j in range(2,i):
        if (i%j==0):
            isPrime=False;
            break            
    if(isPrime==True):
            print i

Add class
HELLo