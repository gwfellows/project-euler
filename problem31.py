"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

# a + 2b + 5c + 10d + 20w + 50e + 100f + 200g = 200
ans = 0
for a in range(200 // 1 + 1):
    currentsum = 1 * a
    if currentsum == 200:
        ans += 1
        break
    for b in range(200 // 2 + 1):
        currentsum = 1 * a + 2 * b
        if currentsum == 200:
            ans += 1
            break
        if currentsum > 200:
            break
        for c in range(200 // 5 + 1):
            currentsum = 1 * a + 2 * b + 5 * c
            if currentsum == 200:
                ans += 1
                break
            if currentsum > 200:
                break
            for d in range(200 // 10 + 1):
                currentsum = 1 * a + 2 * b + 5 * c + 10 * d
                if currentsum == 200:
                    ans += 1
                    break
                if currentsum > 200:
                    break
                for w in range(200 // 20 + 1):
                    currentsum = 1 * a + 2 * b + 5 * c + 10 * d + 20 * w
                    if currentsum == 200:
                        ans += 1
                        break
                    if currentsum > 200:
                        break
                    for e in range(200 // 50 + 1):
                        currentsum = 1 * a + 2 * b + 5 * c + 10 * d + 20 * w + 50 * e
                        if currentsum == 200:
                            ans += 1
                            break
                        if currentsum > 200:
                            break
                        for f in range(200 // 100 + 1):
                            currentsum = (
                                1 * a
                                + 2 * b
                                + 5 * c
                                + 10 * d
                                + 20 * w
                                + 50 * e
                                + 100 * f
                            )
                            if currentsum == 200:
                                ans += 1
                                break
                            if currentsum > 200:
                                break
                            for g in range(200 // 200 + 1):
                                currentsum = (
                                    1 * a
                                    + 2 * b
                                    + 5 * c
                                    + 10 * d
                                    + 20 * w
                                    + 50 * e
                                    + 100 * f
                                    + 200 * g
                                )
                                if currentsum == 200:
                                    ans += 1
                                if currentsum > 200:
                                    break

print(ans)
