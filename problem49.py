def is_prime(n):
	if n == 2:
		return True
	if n < 2 or n % 2 == 0:
		return False

	return all(n % i != 0 for i in range(3, int(n ** 0.5 + 1), 2))


from itertools import permutations

def candidates(n):
	for k in permutations(str(n)):
		if (k := int(''.join(k))) > n:
			for j in permutations(str(n)):
				if (j := int(''.join(j))) == 2*k - n:
					return k, j
	return False


for n in range(1000, 9999+1):
	if is_prime(n):
		if (cand := candidates(n)):
			if is_prime(cand[0]) and is_prime(cand[1]) and ((n, cand[0], cand[1]) != (1487, 4817, 8147)):
				print(str(n) + str(cand[0]) + str(cand[1]))
				break
