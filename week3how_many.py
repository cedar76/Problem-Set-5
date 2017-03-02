# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 00:07:00 2017

@author: Admin
"""
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['a'].append('albatros')
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    res = 0
    for value in aDict.values():
        res += len(value)
    return res
print(how_many(animals))