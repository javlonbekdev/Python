# # -*- coding: utf-8 -*-
# """
# Created on Tue Sep 28 08:52:23 2021

# @author: Javlonbek
# """

# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()

# pi = PI.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
# pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
# pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz
# print(pi)

# with open('pi.txt') as file:
#     for line in file:
#         print(line)

# with open('pi.txt') as file:
#     talabalar = file.readlines()

# print(talabalar)

# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# faylnomi = 'ustozlar.txt'# ochilayotgan (yaratilayotgan) fayl nomi
# with open(faylnomi,'w') as fayl:
#     fayl.write('anvar narzullaev')
    
# faylnomi = 'new_file.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2004
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism)
#     fayl.write(str(tyil))
    
# with open(faylnomi,'a') as fayl:
#     fayl.write('Alijon Valiyev\n')
#     fayl.write('2000')
    
# import pickle

# talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
# talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

# with open('info','wb') as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)
    
# with open('info','rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)

# print(talaba1)

#2-savol
with open('pi_million_digits.txt') as file:
    pi = file.read()
pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
pi = pi.replace(' ','')
birth = '20000131'

print(birth in pi)

while True:
    kitob = input('kitob kiriting: ')
    if not kitob: break
    with open('book.txt', 'a') as file:
        file.write(kitob + '\n')