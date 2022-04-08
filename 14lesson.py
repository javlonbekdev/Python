# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:17:55 2021

@author: Javlonbek
"""

#1-savol
akam = {'ismi':'Javohir', 'yoshi': '25', 'kasbi': 'akfa'}
yosh = (akam['yoshi'])
ism = akam['ismi']
kasb = akam['kasbi']
print(f'{yosh} yoshli {ism} akam {kasb} qiladi')

#2-savol
taom = {'men':'surguruch', 'akam':'manti', 'dadam':'osh','ukam':'shashlik', 'onam':'xonim','opam':'sho\'rva'}
a_taom = taom['akam']
print(f'akamning sevimli taomi {a_taom}')

#3-savol
dicti = {'integer':'butun', 'float':'o\'nli', 'if':'agar'}
i = dicti.get('integer','bunday lug\'at mavjud emas')
k = dicti.get('else', 'bunday lug\'at mavjud emas')
print(i)
print(k)

if dicti.get['else', 'a'] == 'a':
    print(dicti['else'])
else:
    print('Bunday lug\'at mavjud emas')