#!/usr/bin/env python3

"""
Test is made of many functions that represent different tests.
"""

from EquSLPData import *
import csv



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




def TestPremiumA(a,b,c):
    
    """
    Applies EquSLPData to: 
    - a+b*c^(2^n) vs. { a+b*c^(2^(n-1)) ; a+b*c^(2^(n-2)) ; ... ; a+b*c^(2^1) }
    - a+b*c^(2^(n-1)) vs. { a+b*c^(2^(n-2)) ; a+b*c^(2^(n-3)) ; ... ; a+b*c^(2^1) }
    - ...
    - a+b*c^(2^2) vs. a+b*c^(2^1)
    """
    
    # iterations = (n^2 - n) / 2
    n = 64
    # [2^(i - 1), 2^(i) - 1] where i is in [u-1,v]
    u = 8 
    v = 32 
   
    if n < 1 or a < 0 or b < 1 or c < 1 or u < 1 or v < u:
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
                
    


def TestPremiumB(a,b,c,x,y,z):
    
    """
    Applies EquSLPData to:
    - a+b*c^(2^n) vs. { x+y*z^(2^n) ; x+y*z^(2^(n-1)) ; ... ; x+y*z^(2^(1)) }
    - a+b*c^(2^(n-1) vs. { x+y*z^(2^n) ; x+y*z^(2^(n-1)) ; ... ; x+y*z^(2^(1)) }
    - ...
    - a+b*c^(2^1) vs. { x+y*z^(2^n) ; x+y*z^(2^(n-1)) ; ... ; x+y*z^(2^(1)) }   
    """
    
    # iterations = n^2
    n = 64
    # [2^(i - 1), 2^(i) - 1] where i is in [u-1,v]
    u = 8 
    v = 32 
   
    if n < 1 or a < 0 or b < 1 or c < 1 or x < 0 or y < 1 or z < 1 or u < 1 or v < u or (a == x and b == y and c == z):
        return False

    fname = str(a)+"+"+str(b)+"*"+str(c)+"^(2^"+str(n)+") vs. "+str(x)+"+"+str(y)+"*"+str(z)+"^(2^"+str(n)+").csv"
    
    header = ['lenX', 'lenY', "bits", "proba"]
    
    with open(fname, mode='w') as f:
        f_w = csv.writer(f, delimiter=',', 
                         quotechar='"', quoting=csv.QUOTE_MINIMAL)
        f_w.writerow(header)

    

    X = [1]
    for i in range(max(a,b,c)-1):
        
        X.append((i,0,'+'))
          
    Y = [1]
    for i in range(max(x,y,z)-1):
        
        Y.append((i,0,'+'))
        
    
    
    if a == 0 and b == 1:
        
        
        if x == 0 and y == 1:
        
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
        
            
        elif x == 0 and y > 1:
            
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,y-1,'*'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y.pop()
                    
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
        
             
        elif x > 0 and y == 1:
            
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,x-1,'+'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y.pop()
                    
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
        
    
        else:
            
               for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,y-1,'*'))
                    Y.append((Y[-1][0]+1,x-1,'+'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y = Y[:len(Y)-2]
                    
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))



    if a == 0 and b > 1:
        
        
        if x == 0 and y == 1:
        
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,b-1,'*'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                
                X.pop()
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
                        
        
        elif x == 0 and y > 1:
            
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,b-1,'*'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,y-1,'*'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y.pop()
                
                X.pop()
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
        
             
        elif x > 0 and y == 1:
            
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,b-1,'*'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,x-1,'+'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y.pop()
                
                X.pop()
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
        
    
        else:
            
               for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,b-1,'*'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,y-1,'*'))
                    Y.append((Y[-1][0]+1,x-1,'+'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y = Y[:len(Y)-2]
                
                X.pop()
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))



    if a > 0 and b == 1:
        
        
        if x == 0 and y == 1:
        
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,a-1,'+'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                
                X.pop()
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
                        
        
        elif x == 0 and y > 1:
            
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,a-1,'+'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,y-1,'*'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y.pop()
                
                X.pop()
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
        
             
        elif x > 0 and y == 1:
            
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,a-1,'+'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,x-1,'+'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y.pop()
                
                X.pop()
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
        
    
        else:
            
               for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,a-1,'+'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,y-1,'*'))
                    Y.append((Y[-1][0]+1,x-1,'+'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y = Y[:len(Y)-2]
                
                X.pop()
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
        
                
        
    else:
        
        if x == 0 and y == 1:
        
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,b-1,'*'))
                X.append((X[-1][0]+1,a-1,'+'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                
                X = X[:len(X)-2]
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
                        
        
        elif x == 0 and y > 1:
            
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,b-1,'*'))
                X.append((X[-1][0]+1,a-1,'+'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,y-1,'*'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y.pop()
                
                X = X[:len(X)-2]
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
        
             
        elif x > 0 and y == 1:
            
            for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,b-1,'*'))
                X.append((X[-1][0]+1,a-1,'+'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,x-1,'+'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y.pop()
                
                X = X[:len(X)-2]
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))
        
        
        else:
            
               for i in range(n):
                
                X.append((c-1+i,c-1+i,'*'))
                X.append((X[-1][0]+1,b-1,'*'))
                X.append((X[-1][0]+1,a-1,'+'))
                
                for j in range(n):
                
                    Y.append((z-1+j,z-1+j,'*'))
                    Y.append((Y[-1][0]+1,y-1,'*'))
                    Y.append((Y[-1][0]+1,x-1,'+'))
                    RandomProbabilityLimited(X,Y,fname,u,v)
                    Y = Y[:len(Y)-2]
                
                X = X[:len(X)-2]
                Y = [1]
                for k in range(max(x,y,z)-1):
                    
                    Y.append((k,0,'+'))