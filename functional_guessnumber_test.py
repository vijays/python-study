#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 10:40:49 2022

@author: Vijay
"""

import unittest
import functional_guessnumber

class TestGame (unittest.TestCase):

    def test_input_correct(self):
        result = functional_guessnumber.process_guess(5, 5)
        self.assertTrue(result)

    def test_input_incorrect(self):
        result = functional_guessnumber.process_guess(5, 7)
        self.assertFalse(result)
        
    def test_input_range_incorrect(self):
        result = functional_guessnumber.process_guess(5, 11)
        self.assertFalse(result)

    #def test_input_type_incorrect(self):
    #    result = functional_guessnumber.process_guess(5, 'abc')
    #    self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

