# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:42:10 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

def fast_approx_ln(x,n):
    a_0 = (1+x)/2                  
    g_0 = sqrt(x)
    A=zeros([n,n]) # skapar n*n-matris med nollor
    A[0,0]=a_0 # stoppar in a_0 på första platsen (k,i)
    d=a_0 # def d
    
    for i in range(1,n+1): # vi hoppar över element(0,0)           
        a_0 = (a_0+g_0)/2           
        g_0 = sqrt(a_0 + g_0) # här produceras a_0+i, vilket heter a_0
        A[0,i]=a_0 # lägg till a_i på plats i 
        
        for k in range(1,n+1):
            d=(A[i-1,k]-(4**-k)*A[i-1,k-1])/1-4**-k
            A[i,k]=d # lägger till d
    
    return (x-1)/A[n,n]
