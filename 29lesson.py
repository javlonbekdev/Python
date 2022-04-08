# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:57:03 2021

@author: Javlonbek
"""

#1-2-3-savol
class Avto():
    def __init__(self, model, rang, narx, korobka):
        self.model = model
        self.rang = rang
        self.narx  = narx
        self.korobka = korobka
        self.distance = 0
    def get_info(self):
        return f"{self.distance} km yurgan {self.korobka} korobkali {self.rang} {self.model} - {self.narx}$ turadi"
    def update(self):
        self.distance += 100
    
malibu = Avto('Malibu', 'qora', 35000, 'avtomat')
print(malibu.get_info())

malibu.update()
print(malibu.get_info())

#4-5-6-7-savol
class Avtosalon():
    def __init__(self, nom, manzil):
        self.nom = nom
        self.manzil = manzil
        self.avtomobil = []
    def add_amobil(self,amobil):
        self.avtomobil.append(amobil)
      
    def get_amobil(self):
        return [x.get_info() for x in self.avtomobil]
    
asalon = Avtosalon('park', 'quqon')
asalon.add_amobil(malibu)
print(asalon.avtomobil[0].get_info())
print(asalon.get_amobil())

print(dir(Avtosalon))
def see_methods(klass):
    return [method for method in dir(klass) if not method.startswith('__')]

print(see_methods(Avtosalon))