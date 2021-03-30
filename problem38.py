for i in range(9876, 9122, -1):
    s = str(i) + str(i * 2)
    if set(s) == set("123456789"):
        print(s)
        break