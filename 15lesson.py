# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:14:25 2021

@author: Javlonbek
"""

#1-savol
dic = {'integer':'butun', 'boolean': 'mavhum', 'if': 'agar'}
for a,b in sorted(dic.items()):
    print(f'key: {a}')
    print(f'value: {b}\n')
    
#2-savol
countries = {'USA':'Washington', 'UK':'London', 'France':'Paris'}
country = input('Mamlakat kiriting: ')
if country in countries:
    print(countries[country])
else:
    print("hozircha bu mamlakat poytaxtini bilmaymiz!")

#3-savol
taomlar = {'osh':25, 'sho\'rva':15, 'do\'lma':20, 'non':2,'burda':7}
buyurtma = ['non','osh','salat']
for taom in buyurtma:
    if taom in taomlar:
        print(taom, taomlar[taom], ' so\'m')
    else:
        print(f'bizda {taom} yo\'q')