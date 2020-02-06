#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 03:58:09 2020

@author: kevinhowlett
"""

#Function that takes a string and applies the Atbash cipher to it.
#The Atbash cipher is an encryption method in which each letter of a word 
#is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; 
#C <=> X; etc

def atbash(txt):
    import string
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    atbash_dict = {}
    for i in range(13):
        atbash_dict[upper[i]] = upper[25 - i]
        atbash_dict[upper[25 - i]] = upper[i]
        atbash_dict[lower[i]] = lower[25 - i]
        atbash_dict[lower[25 - i]] = lower[i]

    new_string = ''
    for character in txt:
        if character in string.ascii_letters:
            new_string += atbash_dict[character]
        else:
            new_string += character
    return new_string
    
    
    
#Test Cases
atbash("apple") #returns zkkov
atbash("Hello world!") #returns Svool dliow!
atbash("Christmas is the 25th of December") #returns Xsirhgnzh rh gsv 25gs lu Wvxvnyvi
