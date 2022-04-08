# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:44:12 2021

@author: Javlonbek
"""
from talaba_shaxs import Shaxs, Talaba
import unittest

class Shaxs_Test(unittest.TestCase):
    def setUp(self):
        ism = 'Javlonbek'
        fami = 'Muhammad'
        yosh = 12
        self.shaxs1 = Shaxs(ism, fami, yosh)
        self.talaba1 = Talaba(ism, fami, yosh)
    def test_info(self):
        self.assertIsNotNone(self.shaxs1.ism)
    def test_get_info(self):
        shaxs1_info = "Javlonbek Muhammad 12 yoshda "
        self.assertEqual(shaxs1_info, self.talaba1.get_info())
        
unittest.main()