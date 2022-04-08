# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:03:23 2021

@author: Javlonbek
"""

#1-savol
ismlar = ["Davron", "Ulug'bek", "Jonibek"]
print(ismlar[0], "qachon to'y endi")
print(ismlar[1], "dobriysanda urta")

#2-savol
sonlar =[22, 45, 13, 35]
yigindi = sonlar[0] + sonlar[3]
print(yigindi)
sonlar[2] = 51
print(sonlar)

#3-savol
t_shaxslar = ["Muhammad s.a.v", "Abu Bakir r. a.", "Umar r.a.", "Usmon r.a."]
for_me1 = t_shaxslar.pop(0)
z_shaxslar = ["Ilon Mask", "Al-afasy", "Abdulloh domla"]
for_me2 = z_shaxslar.pop(2)
print("Tarixiy shaxslardan ", for_me1 , "ni juda ko'rgim keladi, Zamonamiz shaxslaridan esa ", for_me2, "ni rosa ko'rgim keladi")

#4-savol
friend = []
friend.append("Doniyor")
friend.append("Jahongir")
friend.append("Shodiyor")
friend.append("Davron")
friend.append("Eldor")
print(friend)
friend.remove("Shodiyor")
print(friend)
friend.insert(0, "Doniyor")
friend.insert(3, "Sarvar")
print(friend)
mehmonlar = []
mehmonlar.append(friend.pop(1))
mehmonlar.append(friend.pop(4))
print(mehmonlar)
