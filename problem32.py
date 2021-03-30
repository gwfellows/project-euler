from itertools import permutations

products = set()

for perm in permutations("123456789"):
    base = "".join(perm)
    for splita in range(1, 2 + 1):
        splitb = (9 - splita) // 2 + splita
        a = base[:splita]
        b = base[splita:splitb]
        c = base[splitb:]
        if int(a) * int(b) == int(c):
            products.add(int(c))

print(sum(products))