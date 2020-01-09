#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:11:48 2020

@author: kevinhowlett
"""

#A function that determines whether each seat can "see" the front-stage. A number can "see" 
#the front-stage if it is strictly greater than the number before it.

def can_see_stage(seats):
    for i in range(len(seats[0])):
        column = []
        for j in range(len(seats)):
            column.append(seats[j][i])
        for k in range(len(column)):
            try:
                if column[k] >= column[k+1]:
                    return False
            except IndexError:
                continue
    return True
        
        
print(can_see_stage([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 2, 2], 
               [5, 5, 5, 5, 4, 4], [6, 6, 7, 6, 5, 5]]))