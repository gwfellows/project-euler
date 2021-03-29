import math


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    return all(n % i != 0 for i in range(3, int(math.sqrt(n) + 1), 2))


def get_pairs_that_sum_to(n):
    return ((a, n - a) for a in range(1, n // 2 + 1))


def is_square(n):
    return math.isqrt(n) ** 2 == n


n = 3
while True:
    if not is_prime(n):
        consistent = False
        for pair in get_pairs_that_sum_to(n):
            if (is_prime(pair[0]) and is_square(pair[1] // 2)) or (
                is_prime(pair[1]) and is_square(pair[0] // 2)
            ):
                consistent = True
                break
        if not consistent:
            print(n)
            break
    n += 2