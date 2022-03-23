#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:10:50 2022

@author: q
"""

unbalanced = ["(){]", ")", "{][}",]

balanced = [ "{{}}()[()]", "[()]{}{[()()]()}", 
            "[(])", "[()]{}{[()()]()}", "(()((())()))"]

test_cases = unbalanced + balanced


def isBalanced(case):
    
    # balanced
    balanced = True; brackets = list(case)
    # not balanced if odd length
    if len(brackets) % 2 == 1: balanced = False   
    stack = []
    while brackets and balanced:
        last = brackets.pop(0)
        if last in ['{', '[', '(']:
            stack.append(last)
            
        else:
            if not stack: 
                balanced = False
            else:
                if last == '}' and '{' in stack:
                    stack.remove('{')
                elif last == ']' and '[' in stack:
                    stack.remove('[')
                elif last == ')' and '(' in stack:
                    stack.remove('(')
                else:
                    balanced = False
                    
    return balanced
    

for case in test_cases:
    print('Balanced :', isBalanced(case = case), f' ~> {case}')
            
