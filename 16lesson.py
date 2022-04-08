# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:11:26 2021

@author: Javlonbek
"""

#1-2savol
famous1 = {
    'ism':'Abdulloh domla',
    'yosh':48,
    'kasb':'imom'}
famous2 = {
    'ism':'Muhammadali',
    'yosh':27,
    'kasb':'tadbirkor'}
famous3 = {
    'ism':'Javlonbek',
    'yosh':'22',
    'kasb':'junior programmist'}
famous = [famous1, famous2, famous3]
for fam in famous:
    print(f"{fam['yosh']} yoshli {fam['ism']} hozirda {fam['kasb']}dir")

famous[0]['yonalish'] = 'ma\'ruza aytish'
famous[1]['yonalish'] = 'savdogarlik'
famous[2]['yonalish'] = 'code yozish'
for fam in famous:
    print(f"{fam['ism']} {fam['yonalish']} bilan band")
    
#3-savol
mal = {'Islomjon':['dinozavr','kingkong'],
       'Muhammadsodiq': ['boyka', 'ongbak'],
       'Toir': ['friends','talaba']}
for m,k in mal.items():
    print(f"\n{m}ning yoqtirib ko\'radigan kinolari ", end = '')
    for kino in k:
        print(kino, end = '')
        if kino == k[0]:
            print(' va ', end = '') 


#4-5-savol
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
# for nom, qiymat in davlatlar.items():
#         print(f"\n{nom.title()} poytaxti {qiymat['poytaxt'].title()},"
#               f"yer maydoni {qiymat['maydon']},"
#               f"aholi soni {qiymat['aholi']},"
#               f"pul birligi {qiymat['pul birligi']}")
user_davlat = ['rossiya', 'aqsh', 'angliya']
for users in user_davlat:
    if users in davlatlar:
            qiymat = davlatlar[users]
            print(f"\n{users.title()} poytaxti {qiymat['poytaxt'].title()},"
                  f"yer maydoni {qiymat['maydon']},"
                  f"aholi soni {qiymat['aholi']},"
                  f"pul birligi {qiymat['pul birligi']}")
    else:
            print(f"Bizda {users} haqida ma'lumot mavjud emas")