#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math



X=2**16 + 10
Y=2**16 
Z = X - Y


factorsX=[]
for i in range(1,X+1):
    if X%i==0:
       factorsX.append(i)
factorsX = set(factorsX)
     
  
factorsY=[]
for i in range(1,Y+1):
    if Y%i==0:
       factorsY.append(i)
factorsY = set(factorsY)

interset = factorsX.intersection(factorsY)


factorsZ=[]
for i in range(1,Z+1):
    if Z%i==0:
       factorsZ.append(i)
factorsZ = set(factorsZ)


fails=[]
for i in range (1,X+1):
    if X % i == Y % i:
        fails.append(i)
fails = set(fails)


print(X)
print(Y)
print(Z)
print("interset:",interset)
print("fails:",fails)
print("factorsZ:",factorsZ)
    




"""
X = [1, (0,0,"+"), (1,0,"+"), (2,1,"+"), (3,1,"+"), (1,1,"*"), (5,5,"*"), 
     (6,6,"*"), (7,5,"*"), (2,2,"*"), (8,9,"*"), (10,3,"*"), 
     (11,4,"*"), (12,0,"+")]

# first gate is always 1
modX = [1] # list of all the gates in X modulo R
    
# calculate the modulo R of each gate in X
for i in range(1,len(X)):
  
    if X[i][2] == "*":
        
        modX.append((modX[X[i][0]] * modX[X[i][1]]))
            
    elif X[i][2] == "+":
            
        modX.append((modX[X[i][0]] + modX[X[i][1]]))
    
print(modX[-1])
"""


def get_prime_factors(number):

    prime_factors = []

    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i

    if number > 2:
        prime_factors.append(int(number))

    return prime_factors


#X = 2
#print(get_prime_factors(X))
# [2, 2, 3, 7]

"""
import time
    
X = [1, (0,0,"+"), (1,0,"+"), (2,1,"+"), (3,1,"+"), (4,1,"+"), (5,1,"+"),
     (1,1,"*"), (7,7,"*"), (8,7,"*"), (2,2,"*"), (10,2,"*"), (9,11,"*"), 
     (12,3,"*"), (13,4,"*"), (14,6,"*"), (15,0,"+")]


Y = [1,] 



timer = time.time() 

print(EquSLP(X,Y))
        
print((time.time() - timer), " seconds")

"""









