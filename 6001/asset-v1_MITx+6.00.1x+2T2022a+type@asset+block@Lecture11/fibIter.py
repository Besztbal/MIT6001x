# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:43:04 2023

@author: user
"""

def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i= 0
        fib_ii= 1
        for i in range(n-1):
            tmp= fib_i
            fib_i= fib_ii
            fib_ii= tmp+ fib_ii
        return fib_ii