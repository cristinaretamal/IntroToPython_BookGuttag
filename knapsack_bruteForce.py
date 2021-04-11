# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:51:04 2021

@author: Vanilla
"""
# The 0/1 knapsack problem can be formalized as follows:
# 1. Each item is represented by a pair, <value, weight>.
# 2. The knapsack can accommodate items with a total weight of no more than w.
# 3. A vector, I, of length n, represents the set of available items. Each element of 
# the vector is an item.
# 4. A vector, V, of length n, is used to indicate whether or not each item is taken 
# by the burglar. If V[i] = 1, item I[i] is taken. If V[i] = 0, item I[i] is not taken.
# 5. Find a V that maximizes
# n-1 Sum i =0 V[i]*I[i].value
# subject to the constraint
# n-1 Sum i =0 V[i]*I[i].weight <= w

# 1. Enumerate all possible combinations of items. That is to say, generate all 
# subsets of the set of items. This is called the power set, and was 
# discussed in Chapter 9.
# 2. Remove all of the combinations whose weight exceeds the allowed weight.
# 3. From the remaining combinations choose any one whose value is the largest.

# implementation of this brute-force approach to solving the 0/1 knapsack problem.
#  It uses the classes and functions defined in Figure 17.2 and Figure 17.3, 
# and the function genPowerset defined in Figure 9.5.

## the function genPowerset defined in Figure 9.5
def getBinaryRep(n, numDigits):
 """Assumes n and numDigits are non-negative ints
 Returns a numDigits str that is a binary
 representation of n"""
 result = ''
 while n > 0:
     result = str(n%2) + result
     n = n//2
 if len(result) > numDigits:
     raise ValueError('not enough digits')
 for i in range(numDigits - len(result)):
     result = '0' + result
 return result

def genPowerset(L):
 """Assumes L is a list
 Returns a list of lists that contains all possible
 combinations of the elements of L. E.g., if
 L is [1, 2] it will return a list with elements
 [], [1], [2], and [1,2]."""
 powerset = []
 for i in range(0, 2**len(L)):
     binStr = getBinaryRep(i, len(L))
     subset = []
     for j in range(len(L)):
         if binStr[j] == '1':
             subset.append(L[j])
     powerset.append(subset)
 return powerset

## the classes and functions defined in Figure 17.2 and Figure 17.3
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

def buildItems():
 names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
 values = [175,90,20,50,10,200]
 weights = [10,9,4,2,1,20]
 Items = []
 for i in range(len(values)):
     Items.append(Item(names[i], values[i], weights[i]))
 return Items


# brute-force optimal solution to the 0/1 knapsack problem
def chooseBest(pset, maxWeight, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)

def testBest(maxWeight = 20):
    items = buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print('Total value of items taken=', val)
    for item in taken:
        print(item)

testBest(20)













