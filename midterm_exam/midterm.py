# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:36:46 2023

@author: felhasznalo
"""

def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x*x + b*x + c


def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    returns the sum of the results of evaluating two quadratic equations
    '''
    firstSet=evalQuadratic(a1,b1,c1,x1)
    secondSet=evalQuadratic(a2,b2,c2,x2)
    result=firstSet+secondSet
    
    print(result)
    


def lessThan4(aList):
    '''
    aList: a list of strings
    returns the sublist of strings in aList that contain fewer than 4 characters
    '''
    result=[]
    for elem in aList:
        if len(elem)<4:
            result.append(elem)
    return result

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns a list of keys in aDict that map to integer values that are unique
    '''
    
    values=[]
    uniqueKeys=[]
    uniqueValues=[]    
    for v in aDict.values():
        values.append(v)
    for i in aDict.values():
        if values.count(i)==1:
            uniqueValues.append(i)    
    if len(aDict) == 0:
        return uniqueKeys
    for k,v in aDict.items():
        if v in uniqueValues:
            uniqueKeys.append(k)        
    return sorted(uniqueKeys)

print(uniqueValues({5: 1, 7: 1}))


def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def score(word,f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    if len(word) > 1:
        
        alphabet='abcdefghijklmnopqrstuvwxyz'    
        scoreDict={}
        count=0
        for letter in word:
                index = alphabet.find(letter.lower())+1
            
                if letter in scoreDict: 
                
                        scoreDict[letter] += (index)*count
                
                else:
                
                        scoreDict[letter] = (index)*count
            
                count+=1    
        sortedValues=sorted(scoreDict.values(), reverse=True) 
        if len(sortedValues)==1:
            return f(sortedValues[0],0)
        first= sortedValues[0]
        second = sortedValues[1]
        return f(first,second)
    

def f(a,b):
    """
    a: a positive integer argument
    b: a positive integer argument
    
    returns: the sum of and b
    """
    return a+b
    



print(score('foo',f))

