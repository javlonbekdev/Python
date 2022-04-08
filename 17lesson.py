# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 06:51:25 2021

@author: Javlonbek
"""

#1-savol
savol = 'yaxshi ko\'rgan kitoblarizgizni kiriting'
savol += 'qachonnchi "exit" so\'zini kiritsangiz dastur to\'xtaydi: '
kitob = ''
while kitob != 'exit':
    kitob = input(savol)
    if kitob != 'exit':
        print(kitob)

#2-savol
savol = 'Yoshingizni kiriting: '
k = ''
while k != 'quit':
    k = input(savol)
    if k !='quit':
        if k <='7':
            print('2000so\'m')
        elif k<='18':
            print('3000 so\'m')
        elif k<='65':
            print('10000 so\'m')
        else:
            print('bepul')

#3-savol
