# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 11:02:05 2021

@author: Javlonbek
"""

#1-savol
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for k in cars:
    if k != 'gm':
        print(k.title())
    else:
        print(k.upper())
        
#2-savol
user = input("loginingizni kiriting: ")
if user == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {user}!")

#3-savol
son = float(input("Musbat son kiriting: "))
print(son**(1/2)) if son>=0 else print("Musbat son kiriting!")