#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:25:08 2021

@author: gigi
"""


X=24
Y=9


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


fails=[]
for i in range (1,X+1):
    if X % i == Y % i:
        fails.append(i)
fails = set(fails)

if fails != interset:
    print(X)
    print(Y)
    print(factorsX)
    print(factorsY)
    print(interset)
    print(fails)
        

# 1, 1+1, 2+1, 3*3
# 1, 1+1, 2*2, 4*4, 16+4, 20+4