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
         last = []
         # cast to a binary with n places
         for ix, j in enumerate(format(i, 'b').zfill(L)):
             if j == '1': # include if 1
                last += [elements[ix]]
         yield last
         
allSets = combinations(items = elements)


for i in allSets:
    print(i)

         
