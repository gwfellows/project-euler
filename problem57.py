numer, denom = 3, 2
count = 0
for n in range(1, 1000 + 1):
    if len(str(numer)) > len(str(denom)):
        count += 1
    denom, numer = numer + denom, 2 * denom + numer

print(count)