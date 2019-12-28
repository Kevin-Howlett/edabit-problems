#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:06:13 2019

@author: kevinhowlett
"""

#Function takes a positive integer and calculates how many dots exist in 
#a pentagonal shape around the center dot on the Nth iteration.
#i.e. pentagonal(1)  -> 1
#     pentagonal(2)  -> 6
#     pentagonal(3)  -> 16


def pentagonal(num):
    if num == 1:
        return 1
    else:
        return pentagonal(num - 1) + (num - 1) * 5
    
