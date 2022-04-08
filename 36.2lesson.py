# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:24:00 2021

@author: Javlonbek
"""
import unittest
from name import maxi, fibonachi

class MaxTest(unittest.TestCase):
    def test_max_test(self):
        k = maxi(1,2,3)
        self.assertEqual(k, 3)
        
class FibonachiTest(unittest.TestCase):
    def test_fibonachi(self):
        self.assertTrue(fibonachi(145))
        
unittest.main()
print(maxi(1,2,3)==3)