#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 00:00:12 2020

@author: kevinhowlett
"""

#function that takes a list of numbers or strings and returns a list with the items 
#from the original list stored into sublists. Items of the same value should be in 
#the same sublist

def advanced_sort(lst):
    has_been_encountered = []
    dictionary = {}
    for i in lst:
        if i not in has_been_encountered:
            has_been_encountered.append(i)
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    final_lst = []
    for key in dictionary:
        sub_lst = []
        for i in range(dictionary[key]):
            sub_lst.append(key)
        final_lst.append(sub_lst)
    return final_lst
    

#Test Case
advanced_sort([2, 1, 2, 1])
#returns [[2, 2], [1, 1]]