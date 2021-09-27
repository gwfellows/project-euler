from fractions import Fraction
from functools import cache
from sys import setrecursionlimit

setrecursionlimit(2500)


def expansion(iters):
    @cache
    def term(i, iters):
        return Fraction(1, (2 + term(i + 1, iters))) if i < iters else 0

    return 1 + term(0, iters)


count = 0

for n in range(1, 1000 + 1):
    frac = expansion(n)
    if len(str(frac.numerator)) > len(str(frac.denominator)):
        count += 1

print(count)