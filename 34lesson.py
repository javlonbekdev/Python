# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:14:43 2021

@author: Javlonbek
"""

#1-savol
import json
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)

#2-savol
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
print(talaba['ism'], talaba['familiya'])

#3-savol
t_fam = json.dumps(talaba['familiya'])
t_ism = json.dumps(talaba['ism'])
print(t_ism, t_fam)

#4-savol

with open('students.json') as f:
    talabalar = json.load(f)
print(talabalar)
# print(talabalar[0][0])
for t in talabalar['student']:
    print(t['name'], t['lastname'], t['year'], 'kurs',  t['faculty'], 'talabasi')

#5-savol
with open('api_result.json') as f:
    api = json.load(f)
print(api['query']['pages']['13801']['title'])
print(api['query']['pages']['13801']['extract'])

