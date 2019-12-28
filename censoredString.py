#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:55:27 2019

@author: kevinhowlett
"""

#Function takes in a censored string (censored with * characters) and a string
#of the characters that were censored (in order) and replaces the asterisks to
#uncensor the string

def uncensor(txt, vowels):
    count = 0
    new_txt = ''
    for character in txt:
        if character == '*':
            new_txt += vowels[count]
            count += 1
        else:
            new_txt += character
    return new_txt