# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:32:16 2023

@author: felhasznalo
"""

import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.randrange(0,100,2)

print(genEven())


def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 

print(dist1())

print(dist2())