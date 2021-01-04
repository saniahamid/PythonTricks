# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:54:12 2021

@author: shamid

Context manager is a simple protocol or interface that you object needs to 
follow in order to support the with statement. You need to add __enter__ and
__exit__ methods to an object if you want it to functions as a context manager.

Python will call these two methods at the appropriate times in the resource
management cycle.
"""

class ManagedFile:
    def __init__(self,name):
        self.name = name
        
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            
with ManagedFile('hello.txt') as f:
    f.write('hello, world\n')
    f.write('bye now')
    
    