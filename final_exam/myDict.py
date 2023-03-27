# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:18:12 2023

@author: felhasznalo
"""

class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.dict=[]
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        self.k=k
        self.v=v
        isInList = False
        if len(self.dict) == 0:
            self.dict += [[k,v]]
            isInList = True
        
        for e in self.dict:
            if k == e[0]:
                e[1]=v
                isInList = True
        if isInList == False:
            self.dict += [[k,v]]
            
        
        
    def getval(self, k):
        """ k, immutable object  """
        for e in self.dict:
            if e[0] == k:
                return e[1]
        raise KeyError
        
    def delete(self, k):
        """ k, immutable object """  
        isExist=False
        for e in self.dict:
            if e[0] == k:
                isExist=True
        if isExist==True:
            self.dict=[e for e in self.dict if e[0]!=k]
            return self.dict 
        else:
            raise KeyError
    
    def __str__(self):
        return str(self.dict)
    

md=myDict()
md.assign(1, 2)
print(md)
md.assign(3, 4)
print(md)
md.assign(3, 4)
print(md)
md.assign(3, 7)
print(md)
md.delete(3)
print(md)
# md.delete(3)
print(md)