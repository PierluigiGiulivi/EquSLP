#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def divisors(n):
    
    """
    Author: Tomas Kulich
    url: https://stackoverflow.com/questions/171765/
        what-is-the-best-way-to-get-all-the-divisors-of-a-number
    This function finds all the divisors of an integer
    """
    
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            factors[i] = factors.get(i, 0) + 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, 
                # i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    # in python3, `yield from generate(0)` would also work
    for factor in generate(0):
        yield factor



"""
Creates csv file with the number tested, the bit range and
the amount of divisors in that bit range
"""
import csv

for j in range(22,32):
    
    # start and end of integers that we will test
    start = 2**j + 1
    end = 2**(j+1)
    fname = "divisors"+str(j+1)+".csv"
    
    # create csv file and add header
    header = ["num", "bits", "divisors"]
     
    with open(fname, mode='w') as f:
        f_w = csv.writer(f, delimiter=',', quotechar='"', 
                         quoting=csv.QUOTE_MINIMAL)
        f_w.writerow(header)
                 
    
    # range of values we are testing
    for num in range(start, end + 1):
    
        # translate divisors to their bit length
        bit_length = []
        for i in list(divisors(num)):
            bit_length.append(i.bit_length())
         
        # count how many in each bit range
        for i in range(1, num.bit_length() + 1):
            
            with open(fname, mode='a') as f:
                f_w = csv.writer(f, delimiter=',', quotechar='"', 
                                 quoting=csv.QUOTE_MINIMAL)
                f_w.writerow([num, i, bit_length.count(i) / (2**i - 2**(i-1))]) 