'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
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

def rotation(n):
  rotations = set()
  for i in range( len( str(n) ) ):
    m = int( str(n)[i:] + str(n)[:i] )
    rotations.add(m)
  return rotations

answer = 0
limit = 1000000

is_prime = SieveOfEratosthenes(limit)

for i in range(limit):
    a = rotation(i)
    if sum(map(lambda n: is_prime[n], a)) == len(a):
        answer += 1

print(answer)