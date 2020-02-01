#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 03:08:15 2020

@author: kevinhowlett
"""

#Function returns the simplified version of a fraction

def simplify(txt):
    num_1 = int(txt.split('/')[0])
    num_2 = int(txt.split('/')[1])
    if num_1 < num_2:
        smallest = num_1
    else:
        smallest = num_2
    gcd = 0
    for i in range(smallest):
        if num_1 % (i + 1) == 0 and num_2 % (i + 1) == 0:
            gcd = i + 1
    if num_1 % num_2 == 0:
        return str(int(num_1 / num_2))
    else:
        return str(int(num_1 / gcd)) + '/' + str(int(num_2 / gcd))
    
    
#Test cases
simplify("4/6") #returns '2/3'
simplify("10/11") #returns '10/11'
simplify("100/400") #returns '1/4'
simplify("8/4") #returns '2'
