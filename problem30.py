print(
    sum((n if sum(int(d) ** 5 for d in str(n)) == n else 0) for n in range(2, 10 ** 6))
)
