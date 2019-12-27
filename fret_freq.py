#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:12:00 2019

@author: kevinhowlett
"""

#Function takes in a guitar string number and fret number
#(E standard tuning) and returns the resulting frequency

def fret_freq(g_str, fret):
    if g_str == 1:
        string_frequency = 329.63
    elif g_str == 2:
        string_frequency = 246.94
    elif g_str == 3:
        string_frequency = 196
    elif g_str == 4:
        string_frequency = 146.83
    elif g_str == 5:
        string_frequency = 110
    elif g_str == 6:
        string_frequency = 82.41
    return round(string_frequency * 2**(fret/12), 2)
