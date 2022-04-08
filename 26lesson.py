# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:16:53 2021

@author: Javlonbek
"""

import random as r
from uzwords import words

def get_word():
    return r.choice(words)

def play():
    word = get_word()
    new_word = ''
    while True:
        a = input("so'zni toping: ")
        b = 0
        if a == word(b):
            new_word += a
        else:
            new_word += '-'
    

