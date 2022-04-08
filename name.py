# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:23:03 2021

@author: Javlonbek
"""

def maxi(a,b,c):
    k = 0
    if a>b and a>c:
        k = a
    elif b>a and b>c:
        k = b
    else:
        k = c
    return k

def fibonachi(l):
    e = 0
    d = [1,1]        
    while True:
        d.append(d[e]+d[e+1])
        e+=1
        if d[e+1] == l:
            return True
            break
        elif d[e+1] > l:
            return False
            break
    
print(fibonachi(89))
        

        