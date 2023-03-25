# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:05:37 2023

@author: user
"""
from math import pi

squares = []

for x in range(10):
    squares.append(x**2)

print(squares)

squares2 = list(map(lambda x: x**2, range(10)))

print(squares2)

squares3= [x**2 for x in range(10)]

print(squares3)


# listcomp combines the elements of two lists if they are not equal

listcomp = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

print(listcomp)

#it is equivalent to:

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
newVec=[x*2 for x in vec]
# filter the list to exclude negative numbers
posVec=[x for x in vec if x >= 0]
# apply a function to all the elements
vecAbs=[abs(x) for x in vec]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
newFruits=[fruit.strip() for fruit in freshfruit]
['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square)
newTuple=[(x, x**2) for x in range(6)]
# the tuple must be parenthesized, otherwise an error is raised
#nested function
roundPi=[str(round(pi,i)) for i in range(6)]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transpose = [[col[i] for col in matrix] for i in range(4)]

#equals to:

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

zipFn= list(zip(*matrix))

print(zipFn)

itemList=[item for item in zip(range(1,4),['sugar','spice','everything nice'])]

print(itemList)


    

    


































