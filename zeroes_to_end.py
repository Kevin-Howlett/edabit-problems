#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:54:23 2019

@author: kevinhowlett
"""

#Function takes a list of numbers and mutates it to move all zeroes
#to the end of the list

def zeroes_to_end(lst):
    zero_count = 0
    for number in lst:
        if number == 0:
            zero_count += 1
    for i in range(zero_count):
        lst.remove(0)
    for i in range(zero_count):
        lst.append(0)
    return lst
