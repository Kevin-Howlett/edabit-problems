#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:55:40 2020

@author: kevinhowlett
"""

#Function returns the SHA-256 hash for a given string

import hashlib

def get_sha256_hash(txt):
	return hashlib.sha256(txt.encode('utf-8')).hexdigest()
    
#Test case
print(get_sha256_hash('password123'))