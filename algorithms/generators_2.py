#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:21:17 2022

@author: q

Combination : is a selection of items from a set 
that has distinct members, such that the 
order of selection does not matter 

The number of k-combinations for all k is the number 
of subsets of a set of n elements. That is 2^n.

Each combination is a path in a binary tree,
with depth equal to the number of elements.

Which is the same as enumerating binary numbers
with n places (0000 if 4 elements) from 0 to n-1

/// Source:
    
https://en.wikipedia.org/wiki/Combination    
    
"""

elements = ['cat', 'dog', 'bird', 
            'worm', 'hawk', 'salmon', 
            'lizard', 'bug', 'chipmunk']

def combinations(items = []):
    # posible sets given by a path in a binary tree  
    # with depth equal to the number of items
    L = len(items)
    # number of 2**number of items
    for i in range(2**L):    
         subset = []
         # cast to a binary with n places
         for index, digit in enumerate(format(i, 'b').zfill(L)):
             # include if 1
             if digit == '1': subset += [items[index]]
         yield subset
         
allSets = combinations(items = elements)

for i in allSets:
    print(i)

def combinations_bitwise(items = []):
    # posible sets given by a path in a binary tree  
    # with depth equal to the number of items
    L = len(items)
    for i in range(2**L):
        subset = []    
        for j in range(L):
            # test that LSB is 1 
            if (i >> j) % 2 == 1:
                subset.append(items[j])
        yield subset
    
bitwiseSets = combinations_bitwise(items = elements)

for i in bitwiseSets:
    print(i)

         
