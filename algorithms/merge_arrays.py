#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:10:31 2022

@author: q

Merging two sorted lists using pointers

"""
a = [1, 3, 5, 63, 544, 56, 7, 79, 0, 1, 3, 5]
b = [5, 2, 4, 5, 9, 4, 3, 2, 6, 3, 1351, 14]

def merge(a, b):
    
    a, b = sorted(a, reverse = True), sorted(b, reverse = True)
    
    La, Lb = len(a), len(b)
    
    c = [ 0 for _ in range( La + Lb )]
    
    i, j, x = 0, 0, 0
    
    I, J = La-1, Lb-1
    
    while i < I or j < J:
        
        if i < I and j < J:
            
            if a[i] > b[j]:
               c[x] = a[i]
               i += 1
            else:
                c[x] = b[j]
                j += 1
                
        elif i < I:
            c[x] = a[i]
            i += 1
        
        else:
            c[x] = b[j]
            j += 1
       
        x += 1
        
    return c


print(merge(a, b))
