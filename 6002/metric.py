# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Item(object):
    def __init__(self):       
        self.itemlist=[]   
        
    def getItems(self):
        return self.itemlist
    
    def addItem(self,name,value,weight):
        if self not in self.itemlist:
            self.itemlist.append([name,value,weight])
    
    def getValue(self,name):
        value=0
        for e in self.itemlist:
            if e[0] == name:
                value=e[1]
        
        return value
    
    def getWeight(self,name):
        weight=0
        for e in self.itemlist:
            if e[0] == name:
                weight=e[2]
        
        return weight
    
    def metric1(self,name):
        return self.getWeight('computer')/self.getValue('computer')
    
    def metric2(self):
        return -(self.getWeight())
    
    def metric3(self):
        return self.getValue()
    
    def __str__(self):
        if self.itemlist == []:
            return '{}'
        result = ''
        for e in self.itemlist:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'
    
l=Item()

l.addItem('dirt',4, 0)
l.addItem('computer',10,30)
l.addItem('fork',5, 1)
l.addItem('ps',0, -10)

print(l)    

print(l.getItems())

print(l.getValue('computer'))
print(l.getWeight('computer'))

print(l.metric1('computer'))

