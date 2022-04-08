# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:15:58 2021

@author: Javlonbek
"""

#1savol
# def mal(ism, familiya, yil, raqam = 0):
#     return {
#         'ism': ism,
#         'familiya':familiya,
#         'yil':yil,
#         'raqam':raqam,
#         'yosh':(2021-yil)}
# print(mal('javlonbek','Muhammad amin', 2000, 91852796))

#2-savol
# mijoz = []
# while True:
#     ism = input('ismingizni kiriting: ')
#     familiya = input('familiyangizni kiriting: ')
#     yil = int(input('yilingizni kiriting: '))
#     raqam = int(input('raqamingizni kiriting: '))
#     def mal(ism, familiya, yil, raqam = 0):
#         return {
#             'ism': ism,
#             'familiya':familiya,
#             'yil':yil,
#             'raqam':raqam,
#             'yosh':(2021-yil)}
#     mijoz.append(mal(ism, familiya, yil, raqam))
#     a = input('siz yana kiritasizmi mijoz? ha/yo\'q: ')
#     if a != 'ha':
#         break
# print(mijoz)

#4-savol
# def aylana(radius):
#     return{
#         'radius':radius,
#         'diametr':2*(radius),
#         'perimetr': (6.29*radius),
#         'yuza':(3.15*radius)}
# print(aylana(5))

#6-savol
list = [1,1]
k = 0
while k<10:
    a = list[-1]
    b = list[-2]
    list.append(a+b)
    print(list[-1], end = ' ')
    k = k+1