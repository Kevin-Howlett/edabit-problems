#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:53:53 2020

@author: kevinhowlett
"""

#Function returns a sorted lsited of integers without using the 
#built-in Python sorting functions

def sort_array(lst):
    for j in range(len(lst)):
        for i in range(len(lst)):
            try:
                if lst[i] > lst[i + 1]:
                    lst.insert(i, lst[i + 1])
                    del lst[i + 2]
            except IndexError:
                continue
    return lst
        
#Test Cases        
sort_array([2, -5, 1, 4, 7, 8])
sort_array([23, 15, 34, 17, -28])