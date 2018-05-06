def _gcd(a, b):
    # import ipdb; ipdb.set_trace()
    while b:
        a, b = b, a % b
        print a, b
    return a
