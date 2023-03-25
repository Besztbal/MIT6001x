# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:24:24 2023

@author: user
"""

def genPrimes():
    primeNumbers = [2]
    yield primeNumbers[0]
    x = 3
    while True:
        if all(x%p != 0 for p in primeNumbers):
            primeNumbers.append(x)        
        if x == primeNumbers[-1]:
            yield primeNumbers[-1]
        x += 2