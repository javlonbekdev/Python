# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:33:44 2021

@author: Javlonbek
"""

kocha = "Bog'bon"
mahalla = "Yangiobod"
tuman = "Bog'dod"
viloyat = "Farg'ona"
manzil = f"{viloyat} viloyati, {tuman} tumani, {mahalla} mahallasi, {kocha} ko'chasi"
print(manzil)

print("iltimos quyidagilarni to'ldirig")
kocha = input("ko'changiz: ")
tuman = input("tumaningiz: ")
viloyat = input("viloyatingiz: ")
print(viloyat + " viloyati " + tuman + " tumani " + kocha + " ko'chasi")
