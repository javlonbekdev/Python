# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:47:04 2021

@author: Javlonbek
"""

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