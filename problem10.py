'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.'''


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

primes = SieveOfEratosthenes(2000000-1)

answer = 0

i = 0
while i < len(primes):
    if primes[i]:
        answer += i
    i += 1

print(answer)