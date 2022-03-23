#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:00:37 2022

@author: q
"""
digits = '01'

def nary_tree(digit = '', path = '', depth = 3, leafs = []):    
    # if digit, add to path
    if digit: path += digit
    # when it hits bottom, stores ancestors in leafs
    if len(path) == depth:
        leafs += [path]
        return path
    else:        
        for i in range(len(digits)):
            # explore each branch
            nary_tree(digit = digits[i], path = path)
    # after all iterations iteration returns
    return leafs

print(nary_tree())
