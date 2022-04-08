# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 10:13:26 2021

@author: Javlonbek
"""

#1-savol
ismlar = ["Ai", "Vali", "Abbos", "Jamshid", "Nozim"]
for ism in ismlar:
    print("salom", ism)
print("Kod", len(ismlar), "marta takrorlandi")

#2-savol
for toq in range(11, 20, 2):
    print(f"{toq} ning kubi {toq**3} ga teng")

#3-savol
kino = []
for k in range(5):
    kino.append(input(f"{k+1}-sevimli kinoyingiz: "))
print(kino)

#4-savol
qiymat = input("bugun necha kishi bilan uchrashdingiz: ")
odamlar = []
for k in range(int(qiymat)):
    odamlar.append(input(f"{k+1}-uchrashganiz: "))
print(odamlar)