#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:49:22 2019

@author: kevinhowlett
"""

#First function finds the additive persistence given a number
#(How many times the digits can be summed together before the new number 
#is only one digit long)
#Second function finds the multiplicative persistence
#(Number of times the given number's digits need to be added together
#before the resulting number is one digit long)

def additive_persistence(n):
    persistence = 0
    while len(str(n)) != 1:
        new_num = 0
        for digit in str(n):
            new_num += int(digit)
        persistence += 1
        n = new_num
    return persistence

def multiplicative_persistence(n):
    persistence = 0
    while len(str(n)) != 1:
        new_num = 1
        for digit in str(n):
            new_num *= int(digit)
        persistence += 1
        n = new_num
    return persistence
        