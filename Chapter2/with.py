# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:14:39 2020

@author: shamid
The with statement csn make code that deals with system resources more readable. 
It also helps you avoid bugs or leak by making it practically impossible  to
forget to clean up or release a resource when it is no longer needed.
"""

f = open("hello.txt",'w')
try:
    f.write('Hello, world')
finally:
    f.close()
    
#The above statement can be written with 'with' as follows:
    

with open('hello.txt', 'w') as f:
    f.write('hello, world')
    
