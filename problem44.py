pents = [(n * (3 * n - 1)) // 2 for n in range(1, 10000)]

_pents = set(pents)


def is_pent(n):
    return n in _pents


from itertools import permutations


for i in permutations(pents, 2):
    a, b = i[0], i[1]
    if is_pent(a + b) and is_pent(a - b):
        D = abs(a - b)
        print(D)
