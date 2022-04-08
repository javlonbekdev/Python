# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:21:00 2021

@author: Javlonbek
"""

#1-savol
def bosh_harf(ismlar):
    b_ism = []
    while ismlar:
        k = ismlar.pop()
        b_ism.append(k.title())
    return b_ism
ot = ['sher', 'jasur', 'jamshid']
print(bosh_harf(ot[:]))
print(ot)

#3-savol
def bahola(ismlar):
    baholar = {}
    for l in ismlar:
        ism = l
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(baholar)
        