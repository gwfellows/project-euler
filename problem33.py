"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""


def canceldigits(numer, denom):
    numer_str, denom_str = str(numer), str(denom)
    if "0" in numer_str or "0" in denom_str:
        return -1
    for a in (0, 1):
        for b in (0, 1):
            if numer_str[a] == denom_str[b]:
                return int(numer_str[1 - a]) / int(denom_str[1 - b])
    return -1


import math

fracs = set()

for numer in range(10, 99 + 1):
    for denom in range(numer + 1, 99 + 1):
        if canceldigits(numer, denom) == (numer / denom):
            fracs.add((numer, denom))

numer = 1
denom = 1
for frac in fracs:
    numer *= frac[0]
    denom *= frac[1]

while (gcd := math.gcd(int(numer),int(denom))) > 1:
    numer,denom = numer//gcd,denom//gcd

print(denom)