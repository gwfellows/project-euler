#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

bigNum = 600851475143

import math

def isPrime(n):
    prime = True
    if n <= 1:
        return False
    if n == 2:
        return True

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return prime

factor = 2

n =  math.floor(math.sqrt(bigNum)) + 1
while n > 0:
	if bigNum % n == 0:
		if isPrime(n):
			print(n)
			exit()
	n -= 1

