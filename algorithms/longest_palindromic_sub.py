#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:05:16 2022

@author: q
"""

test_cases = ['babaab']


def function1(case):
    ispal = lambda x: list(x) == list(x)[::-1]
    L = len(case); isp = 0; result = ['', 0]
    for i in range(L-2):
        for j in range(i+2, L):
            sub = case[i:j]
            if ispal(sub) and len(result[0]) < len(sub):
                result[0] = sub
                result[1] = i
                print(case[i:j], case[j:])

            # print(sub, ispal(sub), result)
   
def function2(case):
    """
    1. get the longest palindromic substring
    2. remove it from string
    3. repeat
    """
    
    if len(case) == 1: 
        return case
    ispal = lambda x: list(x) == list(x)[::-1]
    L = len(case);
    for j in range(2, L):
        sub = case[:j]
        if ispal(sub) and len(case) > 1:
            case = function2(case[j:])      
            
    return case            

def function3(case, pal = []):
    """
    1. get the longest palindromic substring
    2. remove it from string
    3. repeat
    """
    
    if len(case) == 1: 
        return case
    ispal = lambda x: list(x) == list(x)[::-1]
    
    L = len(case);
    for j in range(2, L):
        sub = case[:j]
        if ispal(sub) and len(case) > 1:
            pal += [sub]
            case = function3(case[j:])      
    return pal


if __name__ == '__main__':
    
    for case in test_cases:
        
        for f in [function1, function2, function3]:

            value = f(case)
            print(f.__name__, value)
