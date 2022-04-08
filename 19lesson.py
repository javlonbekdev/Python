# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:23:35 2021

@author: Javlonbek
"""
#1-savol
# def yosh_a(yil):
#     print(2021-yil)
# ism = input('ismingizni kiriting: ')
# yili = int(input('tug\'ilgan yilingizni kiriting: '))
# yosh_a(yili)

#2-savol
# def kv_kub(son):
#     print(f"{son} ni kvadirati {son**2}\n{son}"
#     f" ni kubi {son**3}")
# son = int(input("ihtiyoriy son kiriting: "))
# kv_kub(son)

#3-savol
# def juft_toq(son):
#     if son%2 == 0:
#         print(f'{son} - juft son')
#     else:
#         print(f'{son} -toq son')
# son = int(input("ihtiyoriy son kiriting: "))
# print(juft_toq(son))

#7-savol
boluv = []
def bolinuv(son):
    for k in range(2,11):
        if son%k == 0:
            print(f"{son} {k}ga qoldiqsiz bo'linadi")
son = int(input("ihtiyoriy son kiriting: "))
bolinuv(son)