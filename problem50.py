def sieve_of_eratosthenes(n):
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


is_prime = sieve_of_eratosthenes(1000000)
primes = []
for i, v in enumerate(is_prime):
    if v:
        primes.append(i)
num_primes = len(primes)

maxlen = 0
ans = 0

for index, prime in enumerate(primes):
    for length in range(1, num_primes - index):
        sum_of_primes = sum(primes[i] for i in range(index, index + length))
        if sum_of_primes > 1000000:
            break
        if is_prime[sum_of_primes]:
            if length > maxlen:
                ans = sum_of_primes
                maxlen = length

print(ans)