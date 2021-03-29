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

gcd = math.gcd(int(numer), int(denom))
denom = denom // gcd

print(denom)