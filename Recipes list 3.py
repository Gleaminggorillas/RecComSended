# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:05:54 2020

@author: Tom
"""

'''This programme has 3 functions. First, to keep an inventory of all food in the household. Second, to keep a list of all\
 ingredients required by any one specific recipe. Third, to calculate \
what ingredients, if any, must be bought to produce the recipe(s).'''

from collections import Counter

inv={}

invc=Counter()

class Inventory:
    
    '''A store of all food in the household. Items can be added and taken from this list.'''
    
    status = 'ingredient'
    
    def __init__(self,item,num):
        
        self.item = item
        self.num = num
        
    def addinv(self, item, num)
        
        inv.keys = input 
        
#    def add(item, num):
#        pass
#        if item != isinstance(item, str):
#            str(item)
#        else:
#            print('There was an error. Please re-try command the information in the format (pepper, 3).')
#        
#        if inv.get(item) == True:
#            inv = inv.update{item:num}
#        else: 
#            inv.update[item] = int(num)
#class Recipes:
#    
#        '''A list of recipes which can be added to. '''
#    
#        def __init__:(self, {recipe:*{ingr:num}})
#    
#            self.recipe = {{}}
#            
#        
#           
#class Shopping_List:
#    
#    pass
#    
#    '''The sum of items required to produce the recipes of the user. \
#    It will be given an input of specific recipes, and from their value dictionaries,\
#    shall calculate against the inventory dictionary what must be purchased.'''
#
#
#Inventory.add('pepper', 3)
#
#Inventory.add('onion',2)
#
#print (inv)
#
#
#
#
#rcp = {'Nat\'s Bolognese':{'pork mince':500, 'beef mince':500, 'red wine':300, 'onion':1, 'celery':1, 'carrot':3, 'canned tomatoes':400, 'milk':100, 'thyme':2, },\
#            'Nat\'s Chicken Curry':{'chicken breasts':3, 'rice':200, 'double cream':1, 'chicken stock':400, 'tomatoes, canned':400, 'yoghurt, plain':300, 'garlic':3, \
#            'coriander':1, 'onion':1, 'chilli':1, 'bell pepper':2,}, 'Tom\'s Chicken Pasta':{'chicken breast':3, 'tomatoes, canned':800, 'onion':1, 'carrot':2, 'turmeric':1, \
#            'coriander':1, 'cumin':1, 'chestnut mushrooms':200, 'pasta':300, 'garlic':1, 'fine beans':200}, 'Gordon\'s Chorizo Roast Chicken':{'chorizo':1, 'onion':2, 'garlic':1, \
#            'cannolini beans':400, 'thyme':1, 'tomatoes, dried':150, 'lemon':1, 'paprika':1}, 'Tom\'s Chilli':{'beef mince':800, 'onion':1, 'dark chocolate':50, \
#            'fine Beans':200, 'garlic':1, 'cumin':1, 'paprika':1, 'chilli powder':1, 'coriander':1, 'carrot':2, 'pepper, green':2, 'kidney beans':400, 'chilli':2, \
#            'tomatoes, canned':400, 'beef stock':400, 'red wine':300}