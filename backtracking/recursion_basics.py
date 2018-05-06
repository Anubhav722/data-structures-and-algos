def recursion_fact(n):
    if n == 0:
        return 1
    return n * recursion_fact(n - 1)
