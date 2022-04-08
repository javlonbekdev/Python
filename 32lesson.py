# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:15:27 2021

@author: Javlonbek
"""

#1-savol
# class Shaxs():
#     def __init__(self,ism,fami,yosh, bosqich):
#         self.ism = ism
#         self.fami = fami
#         self.yosh = yosh
#         self.bosqich = bosqich
        
#     def __repr__(self):
#         return f"{self.ism} - {self.fami} "
    
#     def __lt__(self, other_avto):
#         return self.bosqich < other_avto.bosqich
    
#     def get_info(self):
#         return f"{self.ism} {self.fami} {self.yosh}"

# shaxs1 = Shaxs('javlonbek', 'muhammad', 21, 4)
# shaxs2 = Shaxs('islomjon', 'muhammad', 20, 3)
# print(shaxs1)
# print(shaxs1<shaxs2)

#2-savol
class Talaba():
    def __init__(self, ism, fami):
        self.ism = ism
        self.fami = fami
    def get_info(self):
        return f"{self.ism} {self.fami}"
    
    def __repr__(self):
        return f"{self.ism}"

class Fan():
    def __init__(self, nom):
        self.nom = nom
        self.talabalar = []
    
        
    def add_students(self, talaba):
        if isinstance(talaba, Talaba):
            self.talabalar.append(talaba)
    
    def __len__(self):
        return len(self.talabalar)
    
    def __getitem__(self, index):
        return self.talabalar[index]
    
    def __setitem__(self, index, qiymat):
        self.talabalar[index] = qiymat
        
    def __call__(self,*param):
        if param: # agar parametr bo'lsa
            for talaba in param:
                self.add_students(talaba)
        else: # agar parametr bo'lmasa
            return [talaba for talaba in self.talabalar]


talaba1 = Talaba('javlonbek', 'muhammad')
talaba2 = Talaba('islomjon', 'meliboyev')
matem = Fan('matem')
matem.add_students(talaba1)
matem.add_students(talaba2)

print(len(matem))
matem[0] = 'jamshid'
print(matem[0])
print(matem(talaba1))
print(matem())






