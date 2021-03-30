def num_distinct_prime_factors(n):
    prime_factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            prime_factors.add(d)
        d += 1
    if n > 1:
        prime_factors.add(n)
    return len(prime_factors)


i = 0
while True:
    if (
        num_distinct_prime_factors(i)
        == num_distinct_prime_factors(i + 1)
        == num_distinct_prime_factors(i + 2)
        == num_distinct_prime_factors(i + 3)
        == 4
    ):
        print(i)
        break
    i += 1