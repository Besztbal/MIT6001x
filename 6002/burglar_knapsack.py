# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:02:46 2023

@author: user
"""

class Item(object):
    def __init__(self, n, v, w):
        self. name = n
        self.value = v
        self.weight = w
    def get_Name(self):
        return self.name
    def get_Value(self):
        return self.value
    def get_Weight(self):
        return self.weight
    def __str__(self):
        return f'<{self.name},          {self.value},      {self.weight}>'
    
def value(item):
    return item.get_Value()

def weight(item):
    return item.get_Value()

def weight_inverse(item):
    return 1.0/item.get_Weight()

def density(item):
    return item.get_Value()/item.get_Weight()

def greedy(items,max_weight,key_function):
    """ assumes items a list, max_weight >= 0,
    key_function maps elements of items to numbers"""
    items_copy = sorted(items,key=key_function, reverse = True)
    result = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(items_copy)):
        if (total_weight + items_copy[i].get_Weight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].get_Weight()
            total_value += items_copy[i].get_Value()
    return (result, total_value)

def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items =[]
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def test_greedy(items, max_weight, key_function):
    taken, val = greedy(items, max_weight, key_function)
    print('Total value of items taken is', val)
    for item in taken:
        print('    ', item)
    
    
def test_greedys(max_weight = 20):
    items = build_items()
    print('Use greedy by value to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, value)
    print('\nUse greedy by weight to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, weight_inverse)
    print('\nUse greedy by density to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, density)
    

test_greedys()