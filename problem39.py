"""
p = a + b + c
forall
	a ^ 2 + b ^ 2 = c ^ 2
	a = int, b = int, c=int
	a>0, b>0, c>0
"""

from multiprocessing import Pool


def get_num_solutions(p):
    solutions = set()
    for a in range(1, p):
        for b in range(1, p - a):
            for c in range(1, p - b):
                if (a ** 2 + b ** 2 == c ** 2) and (a + b + c == p):
                    solutions.add(tuple(sorted((a, b, c))))
    return len(solutions)


if __name__ == "__main__":
    p = Pool(1000)
    sols = p.map(get_num_solutions, range(1, 1000))
    largest = max(sols)
    print(sols.index(largest) + 1)