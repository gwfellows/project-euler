#what is the 10001st prime number

import math

# P.N.T
# n = 200000
# print(1/math.log(n)*n) 
# 16385.28671818444
# so there are around 16385 prime numbers under 200,000 and 200,000 will be my limit for the sieve

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n):  
        if (prime[p]):       
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime

primes = SieveOfEratosthenes(200000)

counter = 0

for i, n in enumerate(primes):
    if n == True:
        counter += 1
        #print(counter)
    if counter == 10001:
        print(i)
        exit()
        