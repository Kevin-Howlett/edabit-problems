#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:42:36 2020

@author: kevinhowlett
"""

#function that, given an input string, determines if the word can be completed.
#An input string can be completed if additional letters can be added and no letters need to be 
#taken away to match the word. Furthermore, the order of the letters in the input string must be 
#the same as the order of letters in the final word.

def can_complete(initial, word):
    new_word = ''
    count = 0
    for i in range(len(word)):
        try:
            if word[i] == initial[count]:
                new_word += word[i]
                count += 1
        except IndexError:
            break
    return new_word == initial
    
#Test Cases
can_complete('butl', 'beautiful')
#returns True

can_complete('bultz', 'beautiful')
#returns False
