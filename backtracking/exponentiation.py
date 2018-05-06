# Improved algorithm.
# Considering even numbers in the loop.


def exponent_recursion(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = exponent_recursion(x, n / 2)
        return y * y
    else:
        return x * exponent_recursion(x, n - 1)


# def exponent_recursion(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * exponent_recursion(x, n - 1)
