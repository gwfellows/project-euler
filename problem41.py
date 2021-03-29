"""

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    return all(n % i != 0 for i in range(3, int(n ** 0.5 + 1), 2))


from itertools import permutations


for cut in range(9, 0, -1):
    primes = set()
    for i in permutations("123456789"[:cut]):
        n = int("".join(i))
        if is_prime(n):
            primes.add(n)
    if primes != set():
        print(max(primes))
        exit()
