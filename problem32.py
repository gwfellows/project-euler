from itertools import permutations

products = set()

for perm in permutations("123456789"):
    base = "".join(perm)
    for splita in range(1, 2 + 1):
        splitb = (9 - splita) // 2 + splita
        a, b, c = int(base[:splita]), int(base[splita:splitb]), int(base[splitb:])
        if a * b == c:
            products.add(c)

print(sum(products))