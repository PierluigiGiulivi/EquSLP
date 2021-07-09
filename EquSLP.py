#!/usr/bin/env python3

"""
SLP Comparator is used to decide if two arithmetic circuits 
are equal by selecting an appropiate random integer and calculating
each circuit mod that random number. 
"""

import math
# set seed for pseudorandom number generator
from random import seed
from random import randint
seed(8) 



def comparator(x,y):
    
    """
    The comparator function calculates the module of each SLP using
    a new random number. The function will return True if the mod 
    of the two circuts is equal and False otherwise.
    
    Input: two SLPs x and y. All SLPs start with x0 = 1. 
    If x is x0 = 1, x1 = x0 + x0 and x2 = x1 * x1 
    then x = [ 1, (0,0,"+") , (1,1,"*") ].
    """
    
    # calculate the size of the input, this is equal to the number
    # of gates in the SLP excluding the initial input x0 = 1
    size = max( len(x) - 1 , len(y) - 1 )
    
    # generate random integer
    R = randint( 1 , 2**(2**size) )
    
    # first gate is always 1
    modx = [1] # list of all the gates in x mod R
    mody = [1] # list of all the gates in y mod R
    
    
    # calculate the mod of each gate in x
    for i in range(1,len(x)):
  
        if x[i][2] == "*":
        
            modx.append( ( modx[x[i][0]] * modx[x[i][1]] ) % R )
            
        elif x[i][2] == "+":
            
             modx.append( ( modx[x[i][0]] + modx[x[i][1]] ) % R )
    
    
    # calculate the mod of each gate in y
    for i in range(1,len(y)):
        
        if y[i][2] == "*":
        
            mody.append( ( mody[y[i][0]] * mody[y[i][1]] ) % R )
            
        elif y[i][2] == "+":
            
             mody.append( ( mody[y[i][0]] + mody[y[i][1]] ) % R )
             
    
    # the last gate mod R is equal to the whole SLP mod R
    if modx[-1] == mody[-1]: 
        return True 
    else:
        return False