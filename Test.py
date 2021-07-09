#!/usr/bin/env python3

"""
Test is made of many functions that represent different tests.
"""

from EquSLPData import *
import csv



def Test1():
    
    """
    Applies EquSLP to 2^(2^n) vs. 2^(2^(n-1))
    """
    n = 20 # n = #gates of Y and n-1 = #gates of X 
   
    X = [1, (0,0,"+")]
    
    Y = [1, (0,0,"+"), (1,1,"*")]
    
    for i in range(1,n):  # defines the size of X and Y
    
        #TotalProbability(X,Y)
        RandomProbability(X,Y)
        #TotalProbabilityLimited(X,Y)
            
        if i == n-1:
            break  
        
        X.append((i,i,'*'))
        
        Y.append((i+1,i+1,'*'))
      
        

def Test2():
    
    """
    Applies EquSLP to 2 * 2^(2^n) vs. 2^(2^n)
    """
    n = 11 # n = #gates of Y and n-1 = #gates of X 
   
    X = [1, (0,0,"+")]
    
    Y = [1, (0,0,"+"), (1,1,"*")]
    
    for i in range(1,n):  # defines the size of X and Y
    
        #TotalProbability(X,Y)
        #RandomProbability(X,Y)
        TotalProbabilityLimited(X,Y)
            
        if i == n-1:
            break  

        X.append((i,i,'*'))
        
        Y.pop() # remove las element aka *2 the whole SLP
        Y.append((i,i,'*'))
        Y.append((i+1,1,'*')) # add *2 the whole SLP



def Test3():
    
    """
    Applies EquSLP to 2^(2^n) vs. 2^(2^n) + 1
    """
    n = 11 # n = #gates of Y and n-1 = #gates of X 
   
    X = [1, (0,0,"+")]
    
    Y = [1, (0,0,"+"), (1,0,"+")]
    
    for i in range(1,n):  # defines the size of X and Y
    
        #TotalProbability(X,Y)
        #RandomProbability(X,Y)
        TotalProbabilityLimited(X,Y)
            
        if i == n-1:
            break  

        X.append((i,i,'*'))
        
        Y.pop() # remove las element aka +1 the whole SLP
        Y.append((i,i,'*'))
        Y.append((i+1,0,'+')) # add +1 the whole SLP



def Test4():
    
    """
    Applies EquSLP to 2^(2^n) vs. 2^(2^n) + 2
    """
    n = 11 # n = #gates of Y and n-1 = #gates of X 
   
    X = [1, (0,0,"+")]

    Y = [1, (0,0,"+"), (1,1,"+")]
    
    for i in range(1,n):  # defines the size of X and Y
    
        #TotalProbability(X,Y)
        #RandomProbability(X,Y)
        TotalProbabilityLimited(X,Y)
            
        if i == n-1:
            break  

        X.append((i,i,'*'))
        
        Y.pop() # remove las element aka +2 the whole SLP
        Y.append((i,i,'*'))
        Y.append((i+1,1,'+')) # add +2 the whole SLP
        


def Test5():
    
    """
    Applies EquSLP to 2^(2^n) vs. 2^n
    """
    n = 12 # n-1 = #gates of Y and n-1 = #gates of X 
   
    X = [1, (0,0,"+")]
    
    Y = [1, (0,0,"+")]
    
    for i in range(1,n):  # defines the size of X and Y
    
        #TotalProbability(X,Y)
        #RandomProbability(X,Y)
        TotalProbabilityLimited(X,Y)
            
        if i == n-1:
            break  

        X.append((i,i,'*'))
        
        Y.append((i,1,'*'))



def TestOdd3():
    
    """
    Applies EquSLP to 3^(2^n) vs. 2^(2^n)
    """
    n = 11 # n = #gates of Y and n-1 = #gates of X 
   
    X = [1, (0,0,"+")]
    
    Y = [1, (0,0,"+"), (1,0,"+")]
    
    for i in range(1,n):  # defines the size of X and Y
    
        #TotalProbability(X,Y)
        #RandomProbability(X,Y)
        TotalProbabilityLimited(X,Y)
            
        if i == n-1:
            break  

        X.append((i,i,'*'))
        
        Y.append((i+1,i+1,'*'))



def TestOdd5():
    
    """
    Applies EquSLP to 5^(2^n) vs. 2^(2^n)
    """
    n = 11 # n+1 = #gates of Y and n-1 = #gates of X 
   
    X = [1, (0,0,"+")]
    
    Y = [1, (0,0,"+"), (1,0,"+"), (2,1,"+")]
    
    for i in range(1,n):  # defines the size of X and Y
    
        #TotalProbability(X,Y)
        #RandomProbability(X,Y)
        TotalProbabilityLimited(X,Y)
            
        if i == n-1:
            break  
  
        X.append((i,i,'*'))
            
        Y.append((i+2,i+2,'*'))



def TestFactorial():
    
    """
    Applies EquSLP to n!n vs. (n+1)! vs. n!
    """
    
    # X = 8!8, Y = 9!, W = 8!
    
    X = [1, (0, 0, '+'), (1, 0, '+'), (2, 1, '+'), (3, 1, '+'), (1, 1, '*'), (5, 5, '*'), (6, 6, '*'), (7, 5, '*'), (2, 2, '*'), (8, 9, '*'), (10, 3, '*'), (11, 4, '*')]
    
    Y = [1, (0, 0, '+'), (1, 0, '+'), (2, 1, '+'), (3, 1, '+'), (1, 1, '*'), (5, 5, '*'), (6, 5, '*'), (7, 1, '*'), (2, 2, '*'), (9, 9, '*'), (8, 10, '*'), (11, 3, '*'), (12, 4, '*')]
    
    W = [1, (0, 0, '+'), (1, 0, '+'), (2, 1, '+'), (3, 1, '+'), (1, 1, '*'), (5, 5, '*'), (6, 5, '*'), (7, 1, '*'), (2, 2, '*'), (8, 9, '*'), (10, 3, '*'), (11, 4, '*')]
    
    """
    Applies EquSLP to n!n vs. (n+1)!
    """
    # n = 8, X = n!n, Y = (n+1)!, W = n!
   
    X = [1, (0,0,"+"), (1,0,"+"), (2,1,"+"), (3,1,"+"), (1,1,"*"), (5,5,"*"), (6,6,"*"), (7,5,"*"), (2,2,"*"), (8,9,"*"), (10,3,"*"), (11,4,"*")] 
    
    Y = [1, (0,0,"+"), (1,0,"+"), (2,1,"+"), (3,1,"+"), (1,1,"*"), (5,5,"*"), (6,5,"*"), (7,1,"*"), (2,2,"*"), (9,9,"*"), (8,10,"*"), (11,3,"*"), (12,4,"*")]
    
    W = [1, (0,0,"+"), (1,0,"+"), (2,1,"+"), (3,1,"+"), (1,1,"*"), (5,5,"*"), (6,5,"*"), (7,1,"*"), (2,2,"*"), (8,9,"*"), (10,3,"*"), (11,4,"*")]
    
    #RandomProbability(X,Y)
    #RandomProbability(X,W)
    #RandomProbability(Y,W)
    TotalProbabilityLimited(X,Y)
    TotalProbabilityLimited(X,W)
    TotalProbabilityLimited(Y,W)
    #RandomProbability(X,Y)
    #RandomProbability(X,W)
    #RandomProbability(Y,W)
    TotalProbabilityLimited(X,Y)
    TotalProbabilityLimited(X,W)
    TotalProbabilityLimited(Y,W)

    

def TestOdd():
    
    """
    Applies EquSLP to 3^(2^n) vs. 5^(2^n)
    """
    n = 40 # n+1 = #gates of Y and n = #gates of X 
   
    X = [1, (0,0,"+"), (1,0,"+")]
    
    Y = [1, (0,0,"+"), (1,0,"+"), (2,1,"+")]
    
    for i in range(1,n):  # defines the size of X and Y
    
        #TotalProbability(X,Y)
        #RandomProbability(X,Y)
        TotalProbabilityLimited(X,Y)
            
        if i == n-1:
            break  
  
        X.append((i+1,i+1,'*'))

        Y.append((i+2,i+2,'*'))
        


def TestPremium(c):
    
    """
    Applies EquSLP to a+b*c^(2^n) vs. a+b*c^(2^(n-1))
    vs. a+b*c^(2^(n-2)) vs. ... vs. a+b*c^(2^(1))
    """
    n = 64
    a = 0
    b = 1
    #c = 3
    
    # [2^(i - 1), 2^(i) - 1] where i is in [u-1,v]
    u = 8 
    v = 32 
   
    if n < 1 or a < 0 or b < 1 or c < 1:
        return False

    fname = str(a)+"+"+str(b)+"*"+str(c)+"^(2^"+str(n)+").csv"
    
    header = ['lenX', 'lenY', "bits", "proba"]
    
    with open(fname, mode='w') as f:
        f_w = csv.writer(f, delimiter=',', 
                         quotechar='"', quoting=csv.QUOTE_MINIMAL)
        f_w.writerow(header)


    X = [1]
    for i in range(max(a,b,c)-1):
        
        X.append((i,0,'+'))
    
    for i in range(n):
        
        X.append((c-1+i,c-1+i,'*'))
    
     
    if a == 0 and b == 1:

        for _ in range(n):
            
            Y = X
            for _ in range(n):
                
                if len(X) != len(Y):
                    RandomProbabilityLimited(X,Y,fname,u,v)

                if len(Y)-1 == max(a,b,c):
                    break
                
                Y = Y[:len(Y)-1]
                
            X = X[:len(X)-1] 
    
    
    elif a == 0 and b > 1:
        
        for _ in range(n):
        
            X.append((X[-1][0]+1,b-1,'*'))
            
            Y = X
            for _ in range(n):
                
                if len(X) != len(Y):
                    RandomProbabilityLimited(X,Y,fname,u,v)
                
                if len(Y)-2 == max(a,b,c):
                    break
                
                Y = Y[:len(Y)-2]
                Y.append((Y[-1][0]+1,b-1,'*'))
                
            X = X[:len(X)-2] 
            
    
    else:
        
        for _ in range(n):
            
            X.append((X[-1][0]+1,b-1,'*'))
            X.append((X[-1][0]+1,a-1,'+'))
            
            Y = X
            for _ in range(n):
                
                if len(X) != len(Y):
                    RandomProbabilityLimited(X,Y,fname,u,v)

                if len(Y)-3 == max(a,b,c):
                    break
                
                Y = Y[:len(Y)-3]
                Y.append((Y[-1][0]+1,b-1,'*'))
                Y.append((Y[-1][0]+1,a-1,'+'))
                
            X = X[:len(X)-3] 
        
        

#Test1()
#Test2()
#Test3()
#Test4()
#Test5()
#TestOdd3()
#TestOdd5() 
#TestFactorial()
#TestOdd() 
TestPremium(2) 
TestPremium(3)
TestPremium(5)
TestPremium(7) 
TestPremium(11) 
TestPremium(13) 
TestPremium(17)
TestPremium(19)
TestPremium(23) 
TestPremium(29) 
TestPremium(31) 
TestPremium(37) 
TestPremium(41) 
TestPremium(43) 
TestPremium(47) 
TestPremium(53)
TestPremium(59) 
TestPremium(61) 
TestPremium(67) 
TestPremium(71) 
TestPremium(73) 
TestPremium(79) 
TestPremium(83) 
TestPremium(89) 
TestPremium(97) 