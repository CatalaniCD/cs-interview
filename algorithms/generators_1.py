#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:06:48 2022

@author: q
"""

def fiboNumbers():
    a, b = 0, 1
    while True:
        fibo = a + b
        a = b
        b = fibo
        yield fibo
        
fibonacci = fiboNumbers()


for i in range(100):
    
    last = fibonacci.__next__()
    
    print(last)
