#!/usr/bin/env python3

"""
EquSLPData is used to calculate the probability of failure 
of the EquSLP algorithm.
"""

import csv
from random import randint

runs = 1000 # number of times to run test in specific range


def EquSLP(X,Y,R):
    
    """
    EquSLP is used to decide if two Straight Line Programs are 
    equal by simply calculating each arithmetic operation of each
    SLP modulo R. If both SLPs have the same modulo R, then they 
    might be equal. This process is run many times with different 
    R values, if it is always equal, we can conclude that both SLPs
    are equal with high probability and return True; otherwise,
    return False.

    Input: two SLPs X and Y. All SLPs start with 1. 
    If X is x0 = 1, x1 = x0 + x0 and x2 = x1 * x1 
    then X = [1, (0,0,"+"), (1,1,"*")].
    """
    
    # first gate is always 1
    modX = [1] # list of all the gates in X mod R
    modY = [1] # list of all the gates in Y mod R
    
    
    # calculate the mod of each gate in X
    for i in range(1,len(X)):
  
        if X[i][2] == "*":
        
            modX.append( ( modX[X[i][0]] * modX[X[i][1]] ) % R )
            
        elif X[i][2] == "+":
            
             modX.append( ( modX[X[i][0]] + modX[X[i][1]] ) % R )
    
    
    # calculate the mod of each gate in Y
    for i in range(1,len(Y)):
        
        if Y[i][2] == "*":
        
            modY.append( ( modY[Y[i][0]] * modY[Y[i][1]] ) % R )
            
        elif Y[i][2] == "+":
            
             modY.append( ( modY[Y[i][0]] + modY[Y[i][1]] ) % R )
             
    
    # the last gate mod R is equal to the whole SLP mod R
    if modX[-1] == modY[-1]: 
        return True 
    else:
        return False    
  
    
  
def TotalProbability(X,Y,fname):
    
    """
    TotalProbability checks every integer in ranges
    of [2^(i - 1), 2^(i) - 1] up to 2^(2^(n-1)) - 1 
    where n+1 is the full lenght of the SLP. 
    The ranges correspond to all the integers 
    that can be represented using i bits.
    It calculates the probability of failure of each range.
    """

    # checks in blocks of size [2^(i - 1), 2^(i) - 1]
    for i in range(2, 2**(max(len(X), len(Y)) - 2) + 1): 
    
        S = 0 # total number of integers that give a worng result
        for R in range(2**(i - 1), 2**(i)):
            
            if EquSLP(X,Y,R):
                S += 1
            
        probability = S / (2**(i) - 2**(i - 1))

        with open(fname, mode='a') as f:
            f_w = csv.writer(f, delimiter=',', quotechar='"', 
                             quoting=csv.QUOTE_MINIMAL)
            f_w.writerow([len(X), len(Y), i, probability])         



def RandomProbability(X,Y,fname):
    
    """
    RandomProbability pseudorandomly selects "runs" 
    amount of integers from ranges [2^(i - 1), 2^(i) - 1] 
    up to 2^(2^(n-1)) - 1 where n+1 is the full lenght of 
    the SLP. The ranges correspond to all the integers 
    that can be represented using i bits.
    It calculates the probability of failure of each range.
    """

    # checks in blocks of size [2^(i - 1), 2^(i) - 1]
    for i in range(2, 2**(max(len(X), len(Y)) - 2) + 1): 
    
        S = 0 # total number of integers that give a worng result
        for _ in range(runs):
            
            # generate random integer
            R = randint(2**(i - 1), 2**(i) - 1)
            
            if EquSLP(X,Y,R):
                S += 1

        with open(fname, mode='a') as f:
            f_w = csv.writer(f, delimiter=',', quotechar='"', 
                             quoting=csv.QUOTE_MINIMAL)
            f_w.writerow([len(X), len(Y), i, S / runs ])         



def TotalProbabilityLimited(X,Y,fname,u,v):
    
    """
    TotalProbabilityLimited checks every integer in ranges
    of [2^(i - 1), 2^(i) - 1] where i is in [u-1,v].
    The ranges correspond to all the integers 
    that can be represented using i bits.
    It calculates the probability of failure of each range.
    """
    
    # checks in blocks of size [2^(i - 1), 2^(i) - 1]
    for i in range(u, v + 1): 
    
        S = 0 # total number of integers that give a worng result
        for R in range(2**(i - 1), 2**(i)):
            
            if EquSLP(X,Y,R):
                S += 1
            
        probability = S / (2**(i) - 2**(i - 1))

        with open(fname, mode='a') as f:
            f_w = csv.writer(f, delimiter=',', quotechar='"', 
                             quoting=csv.QUOTE_MINIMAL)
            f_w.writerow([len(X), len(Y), i, probability])         
    


def RandomProbabilityLimited(X,Y,fname,u,v):
    
    """
    RandomProbabilityLimited pseudorandomly selects "runs" 
    amount of integers from ranges [2^(i - 1), 2^(i) - 1] 
    where i is in [u-1,v].
    The ranges correspond to all the integers 
    that can be represented using i bits.
    It calculates the probability of failure of each range.
    """
   
    # checks in blocks of size [2^(i - 1), 2^(i) - 1]
    for i in range(u, v + 1): 
    
        S = 0 # total number of integers that give a worng result
        for _ in range(runs):
            
            # generate random integer
            R = randint(2**(i - 1), 2**(i) - 1)
            
            if EquSLP(X,Y,R):
                S += 1

        with open(fname, mode='a') as f:
            f_w = csv.writer(f, delimiter=',', quotechar='"', 
                             quoting=csv.QUOTE_MINIMAL)
            f_w.writerow([len(X), len(Y), i, S / runs ])         