#!/usr/bin/env python3

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

# list form: https://oeis.org/A002201/b002201.txt
SHCN =[2, 
       6, 
       12, 
       60, 
       120, 
       360, 
       2520, 
       5040, 
       55440, 
       720720, 
       1441440,
       4324320, 
       21621600, 
       367567200, 
       6983776800, 
       13967553600, 
       321253732800,
       2248776129600, 
       65214507758400, 
       195643523275200, 
       6064949221531200,
       12129898443062400, 
       448806242393308800, 
       18401055938125660800,
       791245405339403414400, 
       37188534050951960476800,
       185942670254759802384000,
       9854961523502269526352000,
       581442729886633902054768000,
       1162885459773267804109536000, 
       12791740057505945845204896000,
       780296143507862696557498656000,
       2340888430523588089672495968000,
       156839524845080402008057229856000,
       11135606264000708542572063319776000,
       812899257272051723607760622343648000,
       64219041324492086165013089165148192000, 
       834847537218397120145170159146926496000,
       69292345589126960972049123209194899168000]


# create csv file and add header
with open("HCN.csv", mode='w') as f:
    f_w = csv.writer(f, delimiter=',', quotechar='"', 
                     quoting=csv.QUOTE_MINIMAL)
    f_w.writerow(["num", "bits", "divisors"])
         

# range of values we are testing
for num in SHCN:

    # translate divisors to their bit length
    bit_length = []
    for i in list(divisors(num)):
        bit_length.append(i.bit_length())
     
    # count how many in each bit range
    for i in range(1, num.bit_length() + 1):
        
        with open("HCN.csv", mode='a') as f:
            f_w = csv.writer(f, delimiter=',', quotechar='"', 
                             quoting=csv.QUOTE_MINIMAL)
            f_w.writerow([num, i, bit_length.count(i) / (2**i - 2**(i-1))]) 