# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 06:30:09 2021

@author: Javlonbek
"""

#1-savol
# def kop(*sonlar):
#     k = 1
#     for son in sonlar:
#         k = k*son
#     return k
# print(kop(1,2,3,4,5))

# #2-savol
# def talabalar(ism,familiya,**mal):
#     mal['ism'] = ism
#     mal['familiya'] = familiya
#     return mal
# print(talabalar('Javlonbek','ibn alisher', kom='hp' , yosh=23))


#24lesson-savol
mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
print(list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar)))