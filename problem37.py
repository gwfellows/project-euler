"""

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""


def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime


UPPER_BOUND = 1000000
_is_prime = SieveOfEratosthenes(UPPER_BOUND)
is_prime = lambda n: _is_prime[n]


def is_truncatable(n):
    s = str(n)
    ans = all(is_prime(int(s[i:])) for i in range(0, len(s))) and all(
        is_prime(int(s[:i])) for i in range(1, len(s))
    )
    if ans:
        print(n, [int(s[i:]) for i in range(0, len(s))])
    return ans


print(sum((n if is_truncatable(n) else 0) for n in range(9, UPPER_BOUND)))
