# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:44:52 2023

@author: user
"""

def fib_recur(n):
    """ assumes n an int>= 0 """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)