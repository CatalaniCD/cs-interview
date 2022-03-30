#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:30:56 2022

@author: q

Code a Linked lists implementation with all suitable methods

"""

class List():
    
    def __init__(self, value = None):
        self.head = Node(value = value)
        self.set_length(node = self.head)
        pass

    def set_length(self, node):
        self.length = node.index
        pass

    def get_length(self):
        return self.length

    def insert(self, value = None):
        # initial node
        node = self.head
    
        while node != None: # loop until tail
            
            if node.get_value() == None: # if no value add value
                node.set_value(value)
                break
            
            elif node.get_next() == None: # step to next node ^ add node 
                node.set_next(node = Node(value = value))
                break
            
            else:
                node = node.next
            
        self.set_length(node.next)
        pass

    def linear_search(self, value):
        # initial node
        node = self.head
       
        while node != None: # loop until tail
            if node.value == value:
                return True
            else:
                node = node.next
        return False
    
    def get_array(self):
        array = []
        node = self.head
        while node != None:            
            array += [(node.get_value(), node.index)]
            node = node.get_next()
        return array
    
    def reindex(self):
        Node.index = 0; i = 0; 
        node = self.head
        while node != None:            
            node.index = i; i += 1; node = node.get_next()
        pass
    
    def remove_index(self, index = None):
        
        if index > self.get_length():
            return False
        
        node = self.head
        prev = self.head
        while node != None:
            # remove any index
            if node.get_index() == index:
                # remove first index
                if index == 0:
                    self.head = self.head.next
                prev.next = node.get_next()
                break
            else:
                prev = node
                node = prev.get_next()
        self.reindex()
        return 
    
    def reverse_nodes(self):
        # initial test
        if self.head == None or self.head.next == None:
           return 
        # curr, prev        
        prev, curr = None, self.head    
        # PREC : node with next node
        while curr: # iterate until curr -> tail NULL
                # add next node
                next_node = curr.next    
                # ref curr to prev
                curr.next = prev
                # advance prev to curr
                prev = curr
                # advance curr to next
                curr = next_node
        # POST : list with inverted pointers
        self.head = prev
        pass
        
    def __str__(self):
        return str(self.get_array())
    
class Node():
    
    index = 0
    
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.index = Node.index
        Node.index += 1
        pass
        
    def set_value(self, value = None):
        self.value = value
        pass
    
    def set_next(self, node = None):
        self.next = node
        pass
    
    def get_index(self):
        return self.index
    
    def get_next(self):
        return self.next
    
    def get_value(self):
        return self.value 

    
    
if __name__ == '__main__':
    
    
    l = List(0)

    print('Insert Values ...')
    for value in ['a', 'f', 'x', 'a']:
        l.insert(value = value)
    
    print('Get list ~> ', l )

    print('Linear Search ~> value = 1 : ', l.linear_search(value = 1))

    # print('Remove Index : ', l.remove_index(0))

    print('Get list ~> ', l )

    l.reverse_nodes()
    
    print(l)
