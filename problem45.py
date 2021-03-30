n = 144
while True:
    h = n * (2 * n - 1)
    i = ((h * 24 + 1) ** 0.5 + 1) / 6
    if int(i) == i:
        print(h)
        break
    n += 1