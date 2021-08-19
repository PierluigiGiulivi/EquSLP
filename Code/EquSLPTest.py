#!/usr/bin/env python3

"""
EquSLPTest is used to calculate the performance
of the EquSLP algorithm.
"""

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
  
    

def BitSpeed(X,Y,k):
    
    """
    Tests if diferent size R impacts performance.
    Creates csv file with the input lenght, the bit range and
    the run time.
    """
    
    import csv
    from random import randint
    import time
    
    runs = 1000 # number of times to run test in specific range
    
    # create csv file and add header
    with open("BitSpeed"+str(k)+".csv", mode='w') as f:
        f_w = csv.writer(f, delimiter=',', quotechar='"', 
                         quoting=csv.QUOTE_MINIMAL)
        f_w.writerow(["len", "bits", "seconds"])
    
    
    maxi = max(len(X), len(Y)) - 2
    if maxi > 9:
        maxi = 9
    
    for i in range(1, 2**maxi + 1):
        
        timer = time.time() 
        
        for _ in range(runs):
            
            R = randint(2**(i - 1), 2**(i) - 1)
            EquSLP(Y,X,R)
            
        seconds = time.time() - timer
            
        with open("BitSpeed"+str(k)+".csv", mode='a') as f:
            f_w = csv.writer(f, delimiter=',', quotechar='"', 
                             quoting=csv.QUOTE_MINIMAL)
            f_w.writerow([len(X)+len(Y), i, seconds / runs]) 
        

# X = 2^(2^8)
X = [1, (0,0,"+"), (1,1,"*"), (2,2,"*"), (3,3,"*"), (4,4,"*"), (5,5,"*"),
     (6,6,"*"), (7,7,"*"), (8,8,"*")]
    
# Y = 2^(2^8)
Y = [1, (0,0,"+"), (1,1,"*"), (2,2,"*"), (3,3,"*"), (4,4,"*"), (5,5,"*"),
     (6,6,"*"), (7,7,"*"), (8,8,"*")]
    
BitSpeed(X,Y,1) 

# X = 2^(2^100)
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
     (97,97,"*"), (98,98,"*"), (99,99,"*"), (100,100,"*")]

# Y = 2^(2^100)   
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
     (97,97,"*"), (98,98,"*"), (99,99,"*"), (100,100,"*")]
        
BitSpeed(X,Y,2)                
  


def SLPSpeed(maxlen,bits,k):
    
    """
    Tests if diferent size of X and Y impacts performance.
    Creates csv file with the input lenght, the bit range and
    the run time.
    """
    
    import csv
    from random import randint
    import time
    
    runs = 1000 # number of times to run test in specific range
    
    # create csv file and add header
    with open("SLPSpeed"+str(k)+".csv", mode='w') as f:
        f_w = csv.writer(f, delimiter=',', quotechar='"', 
                         quoting=csv.QUOTE_MINIMAL)
        f_w.writerow(["len", "bits", "seconds"])
    
    X = [1, (0,0,"+")]
    Y = [1]
    
    for i in range(1, maxlen + 1):
        
        X.append((i,i,'*'))
        
        timer = time.time() 
        
        for _ in range(runs):
            
            R = randint(2**(bits - 1), 2**(bits) - 1)
            EquSLP(Y,X,R)
            
        seconds = time.time() - timer
            
        with open("SLPSpeed"+str(k)+".csv", mode='a') as f:
            f_w = csv.writer(f, delimiter=',', quotechar='"', 
                             quoting=csv.QUOTE_MINIMAL)
            f_w.writerow([len(X)+len(Y), bits, seconds / runs])   
            

SLPSpeed(500,8,1)