#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 03:11:12 2020

@author: kevinhowlett
"""

#Function that groups a string into parentheses cluster. Each cluster 
#should be balanced.

def split(txt):
    lst = []
    start = 0
    end = 0
    open_count = 0
    closed_count = 0
    for i in txt:
        end += 1
        if i == '(':
            open_count +=1
        elif i == ')':
            closed_count += 1
        if open_count == closed_count:
            lst.append(txt[start:end])
            start = end
    return lst
    
#Test Cases    
split("()()()")
#Returns ["()", "()", "()"]

split("((()))")
#Returns ["((()))"]

split("((()))(())()()(()())")
#Returns ["((()))", "(())", "()", "()", "(()())"]