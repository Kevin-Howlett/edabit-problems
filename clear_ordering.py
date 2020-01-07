#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 18:50:36 2020

@author: kevinhowlett
"""

#Function returns True if a list of pairs are sufficient for a clear 
#ordering of all items.

from itertools import permutations

def clear_ordering(lst):
	for p in permutations(lst):
		if all(p[i][1] == p[i+1][0] for i in range(len(p) - 1)):
			return True
	return False

    
    
#Test Cases
print(clear_ordering([["D", "A"], ["C", "B"], ["A", "C"]]))
#True

print(clear_ordering([["D", "A"], ["B", "A"], ["C", "D"]]))
#False