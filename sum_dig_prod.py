#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:16:54 2019

@author: kevinhowlett
"""

#Function that takes numbers as arguments, adds them together, and 
#returns the product of digits until the answer is only 1 digit long


def sum_dig_prod(*argv):
    num = 0
    for arg in argv:
        num += arg
    while len(str(num)) != 1:
        new_num = 1
        for digit in str(num):
            new_num *= int(digit)
        num = new_num
    return num