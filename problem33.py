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

final_numer, final_denom = 1, 1

for numer in range(10, 99 + 1):
    for denom in range(numer + 1, 99 + 1):
        if canceldigits(numer, denom) == (numer / denom):
            final_numer *= numer
            final_denom *= denom

final_denom //= math.gcd(final_numer, final_denom)
print(final_denom)