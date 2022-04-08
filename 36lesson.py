# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:23:03 2021

@author: Javlonbek
"""

def max(a,b,c):
    k = 0
    if a>b and a>c:
        k = a
    elif b>a and b>c:
        k = b
    else:
        k = c
    return k

print(max(1,2,3))
        