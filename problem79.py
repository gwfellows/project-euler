KEYLOG = [
    "319",
    "680",
    "180",
    "690",
    "129",
    "620",
    "762",
    "689",
    "762",
    "318",
    "368",
    "710",
    "720",
    "710",
    "629",
    "168",
    "160",
    "689",
    "716",
    "731",
    "736",
    "729",
    "316",
    "729",
    "729",
    "710",
    "769",
    "290",
    "719",
    "680",
    "318",
    "389",
    "162",
    "289",
    "162",
    "718",
    "729",
    "319",
    "790",
    "680",
    "890",
    "362",
    "319",
    "760",
    "316",
    "729",
    "380",
    "319",
    "728",
    "716",
]


def compatible(password, keylog):
    for key in keylog:
        for digit in password:
            if len(key) == 0:
                continue
            if digit == key[0]:
                key = key[1:]
        if len(key) > 0:
            return False
    return True


import random

p = "".join(KEYLOG)

def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return "".join(lst)


for _ in range(1000):
    for n in range(0, len(p) + 1):
        newp = p[0:n:] + p[n + 1 : :]
        if compatible(newp, KEYLOG):
            p = newp
            break
        i, j = random.randrange(0, len(p)), random.randrange(0, len(p))
        newp = swap(p, i, j)
        if compatible(newp, KEYLOG):
            p = newp
            break

print(p)