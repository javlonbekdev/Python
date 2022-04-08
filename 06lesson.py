# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:02:43 2021

@author: Javlonbek
"""
#1-savol
son = int(input("ihtiyoriy son kiriting: "))
sonning_kv = son**2
sonning_kub = son**3
print(str(son)+ 'ning kvadirati ' + str(sonning_kv) + ' ga teng\n' + str(son) + ' ning kubi ', str(sonning_kub) + ' ga teng')


#2-savol
yosh = int(input("Yoshingizni kiriting: "))
t_yil = 2021-yosh
print("Siz " + str(t_yil) + "-yilda tug'ilgansiz")


#3-savol
a = float(input("birinchi sonni kiriting: "))
b = float(input("ikkinchi sonni kiriting: "))
print(f"{a}+{b} = ", a+b)
print(f"{a}-{b} = ", a-b)
print(f"{a}x{b} = ", a*b)
print(f"{a}/{b} = ", a/b)