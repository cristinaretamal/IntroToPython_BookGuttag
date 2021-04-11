# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:14:18 2021

@author: Vanilla
"""

# POWER SET

# The function genPowerset(L) returns a list a list of lists that contains all 
# possible combinations of the elements of L. For example, if L is ['a', 'b'], the 
# powerset of L will be a list containing the lists [], ['b'], ['a'], and ['a', 'b'].
# The algorithm is a bit subtle. Consider a list of n elements. We can represent 
# any combination of elements by a string of n 0’s and 1’s, where a 1 represents the 
# presence of an element and a 0 its absence. The combination containing no 
# items would be represented by a string of all 0’s, the combination containing all 
# of the items would be represented by a string of all 1’s, the combination 
# containing only the first and last elements would be represented by 100…001, etc. 
# Therefore generating all sublists of a list L of length n can be done as follows:
# 1. Generate all n-bit binary numbers. These are the numbers from 0 to 2n
# .
# 2. For each of these 2n +1 binary numbers, b, generate a list by selecting 
# those elements of L that have an index corresponding to a 1 in b. F

# small change to tesyt git
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

#L = [1,2]
genPowerset([1,2])

