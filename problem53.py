import math

ans = 0

for n in range(100+1):
	for r in range(n+1):
		if math.comb(n,r) > 1000000:
			ans += 1

print(ans)
