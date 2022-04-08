# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 13:47:13 2021

@author: Javlonbek
"""

#1-2savol
class Web():
    def __init__(self, ism, familiya, email):
        self.ism = ism
        self.familiya = familiya
        self.email = email
    def get_info(self):
        return f"user: {self.ism}, fullname: {self.ism} {self.familiya}, email: {self.email}"

web1 = Web('javlonbek', 'muhammad','qwerty@gmail.com')
web2 = Web('javohir', 'muhammad', 'qqw@gmail.com')
print(web1.email)
print(web1.get_info())
print(web2.get_info())

