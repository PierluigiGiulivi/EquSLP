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
    
    
    
    
    
    
    
    

    
X = [1, (0,0,"+"), (1,1,"*"), (2,2,"*"), (3,3,"*"), (4,4,"*"), (5,5,"*"),
     (6,6,"*"), (7,7,"*"), (8,8,"*"), (9,9,"*"), (10,10,"*"), (11,11,"*"),
     (12,12,"*"), (13,13,"*"), (14,14,"*"), (15,15,"*"), (16,16,"*"),
     (17,17,"*"), (18,18,"*"), (19,19,"*"), (20,20,"*"), (21,21,"*"),
     (22,22,"*"), (23,23,"*"), (24,24,"*"), (25,25,"*"), (26,26,"*"),
     (27,27,"*"), (28,28,"*"), (29,29,"*"), (30,30,"*"), (31,31,"*"),
     (32,32,"*"), (33,33,"*"), (34,34,"*"), (35,35,"*"), (36,36,"*"),
     (37,37,"*"), (38,38,"*"), (39,39,"*"), (40,40,"*"), (41,41,"*"),
     (42,42,"*"), (43,43,"*"), (44,44,"*"), (45,45,"*"), (46,46,"*"),
     (47,47,"*"), (48,48,"*"), (49,49,"*"), (50,50,"*"), (51,51,"*"),
     (52,52,"*"), (53,53,"*"), (54,54,"*"), (55,55,"*"), (56,56,"*"),
     (57,57,"*"), (58,58,"*"), (59,59,"*"), (60,60,"*"), (61,61,"*"),
     (62,62,"*"), (63,63,"*"), (64,64,"*"), (65,65,"*"), (66,66,"*"),
     (67,67,"*"), (68,68,"*"), (69,69,"*"), (70,70,"*"), (71,71,"*"),
     (72,72,"*"), (73,73,"*"), (74,74,"*"), (75,75,"*"), (76,76,"*"),
     (77,77,"*"), (78,78,"*"), (79,79,"*"), (80,80,"*"), (81,81,"*"),
     (82,82,"*"), (83,83,"*"), (84,84,"*"), (85,85,"*"), (86,86,"*"),
     (87,87,"*"), (88,88,"*"), (89,89,"*"), (90,90,"*"), (91,91,"*"),
     (92,92,"*"), (93,93,"*"), (94,94,"*"), (95,95,"*"), (96,96,"*"),
     (97,97,"*"), (98,98,"*"), (99,99,"*"), (100,100,"*"), (101,0,"+")]

Y = [1, (0,0,"+"), (1,1,"*"), (2,2,"*"), (3,3,"*"), (4,4,"*"), (5,5,"*"),
     (6,6,"*"), (7,7,"*"), (8,8,"*"), (9,9,"*"), (10,10,"*"), (11,11,"*"),
     (12,12,"*"), (13,13,"*"), (14,14,"*"), (15,15,"*"), (16,16,"*"),
     (17,17,"*"), (18,18,"*"), (19,19,"*"), (20,20,"*"), (21,21,"*"),
     (22,22,"*"), (23,23,"*"), (24,24,"*"), (25,25,"*"), (26,26,"*"),
     (27,27,"*"), (28,28,"*"), (29,29,"*"), (30,30,"*"), (31,31,"*"),
     (32,32,"*"), (33,33,"*"), (34,34,"*"), (35,35,"*"), (36,36,"*"),
     (37,37,"*"), (38,38,"*"), (39,39,"*"), (40,40,"*"), (41,41,"*"),
     (42,42,"*"), (43,43,"*"), (44,44,"*"), (45,45,"*"), (46,46,"*"),
     (47,47,"*"), (48,48,"*"), (49,49,"*"), (50,50,"*"), (51,51,"*"),
     (52,52,"*"), (53,53,"*"), (54,54,"*"), (55,55,"*"), (56,56,"*"),
     (57,57,"*"), (58,58,"*"), (59,59,"*"), (60,60,"*"), (61,61,"*"),
     (62,62,"*"), (63,63,"*"), (64,64,"*"), (65,65,"*"), (66,66,"*"),
     (67,67,"*"), (68,68,"*"), (69,69,"*"), (70,70,"*"), (71,71,"*"),
     (72,72,"*"), (73,73,"*"), (74,74,"*"), (75,75,"*"), (76,76,"*"),
     (77,77,"*"), (78,78,"*"), (79,79,"*"), (80,80,"*"), (81,81,"*"),
     (82,82,"*"), (83,83,"*"), (84,84,"*"), (85,85,"*"), (86,86,"*"),
     (87,87,"*"), (88,88,"*"), (89,89,"*"), (90,90,"*"), (91,91,"*"),
     (92,92,"*"), (93,93,"*"), (94,94,"*"), (95,95,"*"), (96,96,"*"),
     (97,97,"*"), (98,98,"*"), (99,99,"*"), (100,100,"*"), (101,0,"+")]

import time
timer = time.time() 
print(EquSLP(X,Y))
print((time.time() - timer), " seconds")