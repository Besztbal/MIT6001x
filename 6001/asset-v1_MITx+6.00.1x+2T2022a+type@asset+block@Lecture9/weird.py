# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 12:00:14 2023

@author: user
"""

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        x=7
        return x 
    def getY(self):
        y=8
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(X, Y)
print(w1.getX())

w2 = Wild(X, Y)
print(w2.getX())

w3 = Wild(17, 18)
print(w3.getX())

w4 = Wild(X, 18)
print(w4.getX())

X = w4.getX() + w3.getX() + w2.getX()
print(X)