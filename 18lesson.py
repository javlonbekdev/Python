# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:44:40 2021

@author: Javlonbek
"""




#1-savol
# box = []
# while True:
#     b = input('mahsulot kiriting: ')
#     if b != 'shu':
#         box.append(b)
#     else:
#         break
# print(box)

#2-savol
# ebozor = {}
# savol = 'mahsulot nomini kiriting: '
# while True:
#     k = input(savol)
#     ebozor[k] = input('narxni kiritng: ')
#     ques = input('yana mahsulot kiritasmi: ')
#     if ques != 'ha':
#         break

#3-savol
royxat = ['sut', 'non', 'shakar']
ebozor = {'non':2, 'shakar':8, 'gosht':40, 'sabzi':8  }
while royxat:
    royxa = royxat.pop()
    if royxa in ebozor:
        print(f"{royxa} {ebozor[royxa]} so'm")
    else:
        print(f"bizda {royxa} yo'q")