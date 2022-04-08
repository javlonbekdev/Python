# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 12:43:48 2021

@author: Javlonbek
"""

#1-savol
yosh = int(input("Yoshingizni kiriting: "))
if yosh<4 or yosh>60:
    print("Sizga kirish bepul")
elif yosh<18:
    print("kirish 10ming so'm")
else: print("kirish 20ming so'm")

#2-savol
mahsulotlar = ['sabzi', 'piyoz', 'anor', 'rayxon', 'yog\'', 'qaymoq', 'go\'sht', 'tuxum', 'tamat', 'shakar','tuz']
savat = ['kartoshka', 'yog\'', 'non', 'tuxum', 'shakar']
if savat:
    for mahs in savat:
        if mahs in mahsulotlar:
            print(f"{mahs} marketda bor")
        else:
            print(f"Kechirasiz marketda {mahs} yo\"q")
else:
    print("Savat bo\"sh")


    
#3-savol
users = ['jamshid', 'islomjon', 'nizomiddin', 'javlonbek', 'asror']
user = input('login kiriting: ')
if user in users:
    print('login band, boshqa login kiriting!')
else:
    print(f'Xush kelibsiz {user}')

#4-savol
son = int(input("Natural son kiriting: "))
b_sonlar = []
for k in range(2,11):
    if son%k == 0:
        b_sonlar.append(k)
print(f"{son} - {b_sonlar} sonlariga qoldiqsiz bo'linadi!")