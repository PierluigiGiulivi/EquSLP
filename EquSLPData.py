#!/usr/bin/env python3

"""
EquSLPData is used to calculate the probability of failure 
of the EquSLP algorithm.
"""

import csv
# set seed for pseudorandom number generator
from random import seed
from random import randint
seed(8) 

TEST = 1000 # number of times to run test in specific range



def EquSLP(X,Y,R):
    
    """
    The comparator function calculates the module of each SLP using
    a random number R. The function will return True if the mod 
    of the two circuts is equal and False otherwise.
    
    Input: two SLPs X and Y and a random number R. 
    All SLPs start with x0 = 1. 
    If X is x0 = 1, x1 = x0 + x0 and x2 = x1 * x1 
    then X = [ 1, (0,0,"+") , (1,1,"*") ].
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
  
    
  
def TotalProbability(X,Y):
    
    """
    TotalProbability checks every integer in ranges of 
    [2^(i - 1), 2^(i) - 1] up to 2^(2^(n-1)) - 1 
    where n+1 is the size of the SLP. 
    The ranges correspond to all the integers 
    that can be represented using i bits.
    It calculates the probablity of failure of each range.
    """
    
    f = open("TestResult.txt", "a")
    print('', file=f)
    print('TotalProbability', file=f)
    print(X, file=f)
    print(Y, file=f)
    
    for i in range(2, 2**(max(len(X), len(Y)) - 2) + 1): 
        # checks in blocks of size [2^(i - 1), 2^(i) - 1]
        
        S = 0 # total number of integers that give a worng result
        for R in range(2**(i - 1), 2**(i)):
            
            if EquSLP(X,Y,R):
                S += 1
            
        probability = S / (2**(i) - 2**(i - 1))
        print('Range: [ 2 ^',i-1,', 2 ^',i,')',
              'Total Probability = ',probability, file=f)
    
    f.close()



def RandomProbability(X,Y):
    
    """
    RandomProbability pseudorandomly selects TEST amount 
    of integers from ranges [2^(i - 1), 2^(i) - 1] 
    up to 2^(2^(n-1)) - 1 where n is the size of the SLP. 
    The ranges correspond to all the integers 
    that can be represented using i bits.
    It calculates the probablity of failure of each range.
    """
    
    f = open("TestResult.txt", "a")
    print('', file=f)
    print('RandomProbability', file=f)
    print(X, file=f)
    print(Y, file=f)
        
    for i in range(2, 2**(max(len(X), len(Y)) - 2) + 1): 
    # checks in blocks of size [2^(i - 1), 2^(i) - 1]
    
        S = 0 # total number of integers that give a worng result
        for _ in range(TEST):
            
            # generate random integer
            R = randint(2**(i - 1), 2**(i) - 1)
            
            if EquSLP(X,Y,R):
                S += 1
            
        probability = S / TEST
        print('Range: [ 2 ^',i-1,', 2 ^',i,')',
              'Random Probability = ',probability,  file=f)
    
    f.close()



def TotalProbabilityLimited(X,Y):
    
    """
    TotalProbabilityLimited checks every integer in ranges of 
    [2^(i - 1), 2^(i) - 1] where i is in [14,18].
    The ranges correspond to all the integers 
    that can be represented using i bits.
    It calculates the probablity of failure of each range.
    """
    
    f = open("TestResult.txt", "a")
    print('', file=f)
    print('TotalProbabilityLimited', file=f)
    print(X, file=f)
    print(Y, file=f)
    
    for i in range(14, 18 + 1): 
        # checks in blocks of size [2^(i - 1), 2^(i) - 1]
        
        S = 0 # total number of integers that give a worng result
        for R in range(2**(i - 1), 2**(i)):
            
            if EquSLP(X,Y,R):
                S += 1
            
        probability = S / (2**(i) - 2**(i - 1))
        print('Range: [ 2 ^',i-1,', 2 ^',i,')',
              'Total Probability = ',probability, file=f)
    
    f.close()



def RandomProbabilityLimited(X,Y,fname,u,v):
    
    """
    RandomProbabilityLimited pseudorandomly selects TEST amount 
    of integers from ranges [2^(i - 1), 2^(i) - 1] 
    where i is in [u-1,v].
    The ranges correspond to all the integers 
    that can be represented using i bits.
    It calculates the probablity of failure of each range.
    """

    data = [len(X), len(Y)]    
    for i in range(u, v + 1): 
    # checks in blocks of size [2^(i - 1), 2^(i) - 1]
    
        S = 0 # total number of integers that give a worng result
        for _ in range(TEST):
            
            # generate random integer
            R = randint(2**(i - 1), 2**(i) - 1)
            
            if EquSLP(X,Y,R):
                S += 1

        with open(fname, mode='a') as f:
            f_w = csv.writer(f, delimiter=',', quotechar='"', 
                             quoting=csv.QUOTE_MINIMAL)
            f_w.writerow([len(X), len(Y), i, S / TEST ])         