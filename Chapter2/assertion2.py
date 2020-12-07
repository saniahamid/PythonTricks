# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:58:37 2020

@author: shamid
"""

cond = 'z' # ['x', 'y', 'z'] # z will print AssertionError

if cond == 'x':
    print(cond)
    
elif cond == 'y':
    print(cond)

else:
    assert False, ("This could never happen but it did")    
