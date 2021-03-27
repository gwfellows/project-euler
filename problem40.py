num = 1
pos = 1
ans = 1

while True:
    for i in str(num):
        pos += 1
        if pos in (2, 11, 101, 1001, 10001, 100001, 1000001):
            ans *= int(i)
            if pos == 1000001:
                print(ans)
                exit()
    num += 1
