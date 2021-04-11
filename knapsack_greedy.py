# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:43:03 2021

@author: Vanilla
"""

# KNAPSACK PROBLEM

# Greedy Algorithms

#first define class Item. Each Item has a name, 
# value, and weight attribute.

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
            return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
            + ', ' + str(self.weight) + '>'
        return result

def value(item):
 return item.getValue()

def weightInverse(item):
 return 1.0/item.getWeight()

def density(item):
 return item.getValue()/item.getWeight()

def buildItems():
 names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
 values = [175,90,20,50,10,200]
 weights = [10,9,4,2,1,20]
 Items = []
 for i in range(len(values)):
     Items.append(Item(names[i], values[i], weights[i]))
 return Items


# The only interesting code is the implementation of the function greedy. By 
# introducing the parameter keyFunction, we make greedy independent of the 
# order in which the elements of the list are to be considered. All that is required 
# is that keyFunction defines an ordering on the elements in items. We then use 
# this ordering to produce a sorted list containing the same elements as items. 

def greedy(items, maxWeight, keyFunction):
 """Assumes Items a list, maxWeight >= 0,
 keyFunction maps elements of Items to floats"""
 itemsCopy = sorted(items, key=keyFunction, reverse = True)
 result = []
 totalValue = 0.0
 totalWeight = 0.0
 for i in range(len(itemsCopy)):
     if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
         result.append(itemsCopy[i])
         totalWeight += itemsCopy[i].getWeight()
         totalValue += itemsCopy[i].getValue()
 return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
 taken, val = greedy(items, constraint, keyFunction)
 print('Total value of items taken = ', val)
 for item in taken:
     print(' ', item)

def testGreedys(maxWeight = 20):
 items = buildItems()
 print ('Use greedy by value to fill knapsack of size', maxWeight)
 testGreedy(items, maxWeight, value)
 print ('\nUse greedy by weight to fill knapsack of size', maxWeight)
 testGreedy(items, maxWeight, weightInverse)
 print ('\nUse greedy by density to fill knapsack of size', maxWeight)
 testGreedy(items, maxWeight, density)


testGreedys(20)
