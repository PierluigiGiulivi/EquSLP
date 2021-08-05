#!/usr/bin/env python3

import math
# set seed for pseudorandom number generator
from random import seed
from random import randint
seed(8) 


def EquSLP(X,Y):
    
    """
    EquSLP is used to decide if two Straight Line Programs are 
    equal by simply choosing a random "large enough" integer, R, 
    and calculate each arithmetic operation of each SLP modulo R.
    If both SLPs have the same modulo R then they might be equal.
    This porcess is run many times with different R values,
    if it is always equal we can conclude that both SLPs are equal
    with high probability and return True, otherwise return False.

    Input: two SLPs X and Y. All SLPs start with 1. 
    If X is x0 = 1, x1 = x0 + x0 and x2 = x1 * x1 
    then X = [1, (0,0,"+"), (1,1,"*")].
    """
    
    # number of times we run the algorithm
    runs = 1000
    
    # calculate an appropiate amount of bits for the random 
    # integer R depending on the size of the input
    bits = math.floor((max(len(X), len(Y)) - 3))
    
    S = 0 # counts how many times we think they are eqaul
    for _ in range(runs):

        # generate random integer
        R = randint(2**(bits - 1) , 2**(bits))
        
        # first gate is always 1
        modX = [1] # list of all the gates in X modulo R
        modY = [1] # list of all the gates in Y modulo R
        
        
        # calculate the modulo R of each gate in X
        for i in range(1,len(X)):
      
            if X[i][2] == "*":
                
                modX.append((modX[X[i][0]] * modX[X[i][1]]) % R)
                
            elif X[i][2] == "+":
                
                 modX.append((modX[X[i][0]] + modX[X[i][1]]) % R)
        
        
        # calculate the modulo R of each gate in Y
        for i in range(1,len(Y)):
            
            if Y[i][2] == "*":
            
                modY.append((modY[Y[i][0]] * modY[Y[i][1]]) % R)
                
            elif Y[i][2] == "+":
                
                 modY.append((modY[Y[i][0]] + modY[Y[i][1]]) % R)
                 
        
        # the last gate modulo R is equal to the whole SLP modulo R
        if modX[-1] == modY[-1]: 
            S += 1
    
    if S  == runs:
        return True
    else:
        return False