# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:09:12 2023

@author: felhasznalo
"""

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    
    # neg_flag = False
    # if n < 0:
        
    #     neg_flag = True
        
    # if neg_flag == True:
        
    #     raise ValueError 
    
    high = n//6+1
    
    for a in range(high):
        for b in range(high):
            for c in range(high):
                if (6*a+9*b+20*c==n):
                    return True
    return False

def McNuggets2(n):
        
    
    remainder = 0
    a = 20
    b = 9
    # c = 6
    if n%a == 0:
        return True
    else:
        remainder = n%a
    if remainder%b==0:
        return True
    else:
        remainder=remainder%b
    if remainder%6==0:
        return True
    else:
        return False
    

print(McNuggets(155))
print(McNuggets(16))
print(McNuggets(5))
print(McNuggets(18))

print()
print()

print(McNuggets2(155))
print(McNuggets2(16))
print(McNuggets2(5))
print(McNuggets2(18))

