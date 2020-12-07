# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:11:32 2020

@author: shamid

This code shows an example of "assert" statement.
It is a debuggin aid that tests a condition. 
If the assert condition is true then nothing happens and the program continues 
to execute as normal. But if the condition evaluated to false, an
AssertionError is raised with an optional error message.
It is a debugging aid
"""

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Adidas Continental 80s', 'price': 14900}

####### No Error #########
#apply_discount(shoes, 0.25)

####### Error #########
# This call thorws and error because the discount applied in 200%
apply_discount(shoes, 2.0)