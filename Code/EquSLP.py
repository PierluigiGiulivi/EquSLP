#!/usr/bin/env python3

import math
from random import randint

def EquSLP(X,Y):
    
    """
    EquSLP is used to decide if two Straight Line Programs are 
    equal by simply choosing a random "large enough" integer, R, 
    and calculate each arithmetic operation of each SLP modulo R.
    If both SLPs have the same modulo R, then they might be equal.
    This process is run many times with different R values,
    if it is always equal, we can conclude that both SLPs are equal
    with high probability and return True; otherwise, return False.

    Input: two SLPs X and Y. All SLPs start with 1. 
    If X is x0 = 1, x1 = x0 + x0 and x2 = x1 * x1 
    then X = [1, (0,0,"+"), (1,1,"*")].
    """

    # calculate an appropiate amount of bits for the random 
    # integer R and runs depending on the size of the input 
    if max(len(X), len(Y)) - 2 < 900:
        runs = 30
        bits = 30
    else:
        runs = math.ceil(math.sqrt(max(len(X), len(Y)) - 2))
        bits = math.ceil(math.sqrt(max(len(X), len(Y)) - 2))
        
    
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
        if modX[-1] != modY[-1]: 
            return False
    
    return True      