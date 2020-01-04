#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:11:47 2019

@author: kevinhowlett
"""

#Function that returns True if, for each pair of consecutive strings, the 
#second string can be formed from the first by adding a single letter either 
#at the beginning or end


def can_build(lst):
    for i in range(len(lst)):
        try:
            if not lst[i] in lst[i + 1] or not len(lst[i + 1]) - len(lst[i]) == 1:
                return False
        except IndexError:
            continue
    return True
    
#Test Cases
print(can_build(["a", "at", "ate", "late", "plate", "plates"]))
#returns True

print(can_build(["a", "at", "ate", "late", "plate", "plater", "platter"]))
#returns False