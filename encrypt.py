#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:55:31 2019

@author: kevinhowlett
"""

#Function encrypts strings using a method that reverses
#the string and replaces vowels with specified numbers

def encrypt(word):
    vowels = {'a':'0', 'e':'1', 'o':'2', 'u':'3'}
    encrypted_word = ''
    for i in range(len(word)):
        if word[-i-1] in vowels:
            encrypted_word += vowels[word[-i-1]]
        else:    
            encrypted_word += word[-i-1]
    encrypted_word += 'aca'
    print(encrypted_word)

#Tests
encrypt('apple')
encrypt('banana')
encrypt('karaca')
encrypt('burak')
encrypt('alpaca')