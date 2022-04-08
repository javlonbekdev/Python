# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:58:40 2021

@author: Javlonbek
"""

x, y = 5, 8
try:
    a = x/(y-8)
except ZeroDivisionError:
    print('nolga bo\'lib bo\'lmaydi!')

user = {"username":"sariqdev",
        "status":"admin",
        "email":"admin@sariq.dev",
        "phone":"99897123456"}

try:
    us = user['statu']
except KeyError:
    print('bunday kalit yo\'q')
    
file = 'dat.txt'
try:
    with open(file) as f:
        text = f.read()
except FileNotFoundError:
    print('iltimos fileni to\'g\'ri kiriting!')
    
import json
files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)        
    except FileNotFoundError:
        print(f"{filename} mavjud emas")
    else:
        print(talaba['ism'])
        # fayl ustida turli amallar
        
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break        

print(f"Siz {2021-yosh} yilda tug'ilgansiz")