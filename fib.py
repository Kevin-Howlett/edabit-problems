#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 02:24:50 2020

@author: kevinhowlett
"""

#Function uses recursion to return a value in the fibonacci sequence,
#given an index number

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)

#Test Cases
print(fibonacci(7))#returns 13
print(fibonacci(3))#returns 2
print(fibonacci(0))#returns 0