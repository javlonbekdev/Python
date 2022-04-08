# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 22:36:54 2021

@author: Javlonbek
"""
#1-5savol
class Shaxs():
    def __init__(self,ism,fami,yosh):
        self.ism = ism
        self.fami = fami
        self.yosh = yosh
    def get_info(self):
        return f"{self.ism} {self.fami} {self.yosh} yoshda " 
        
class Talaba(Shaxs):
    def __init__(self, ism, fami, yosh):
        super().__init__(ism, fami, yosh)
        self.fanlar = []
    def add_fan(self, fan):
        self.fanlar.append(fan)
        return self.fanlar
    def get_fan(self):
        return [fan.nom for fan in self.fanlar]
    def remove_fan(self,fan):
        self.fanlar.remove(fan)
        
class Fan():
    def __init__(self, nom):
        self.nom = nom

matem = Fan('Matematika')
adabiyot = Fan('Adabiyot')
talaba = Talaba('Javlonbek', 'muhammad', 21)
talaba.add_fan(matem)
talaba.add_fan(adabiyot)

#8-9savol
class User(Shaxs):
    def __init__(self, ism, fami, yosh, company):
        super().__init__(ism, fami, yosh)
        self.company = company

class Admin(User):
    def __init__(self, ism, fami, yosh, company, parol):
        super().__init__(ism, fami, yosh,company)
        self.parol = parol
    def ban_user(self):
        return f'{self.ism} bloklandi'
user = Admin('rustam', 'qosimov', 27, 'building', 'jorshua')
print(user.ban_user())