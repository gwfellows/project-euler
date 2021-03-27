from multiprocessing import Pool


def get_num_solutions(p):
    nsols = 0
    for a in range(1, p):
        for b in range(1, p - a):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2:
                nsols += 1
    return nsols


if __name__ == "__main__":
    p = Pool(50)
    sols = p.map(get_num_solutions, range(1, 1000 + 1))
    largest = max(sols)
    print(sols.index(largest) + 1)