# Recursion with memoization

memory = {}


def fibonacci(n):
    if n <= 1:
        return n

    if n in memory: # storing the results in the memory.
        return memory[n]
    else:
        f = (fibonacci(n - 1) + fibonacci(n - 2))
        memory[n] = f
        return f


# Using recursion

# def fibonacci(n):
#     if(n <= 1):
#         return n
#     else:
#         return(fibonacci(n - 1) + fibonacci(n - 2))

# n = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(n):
#     print fibonacci(i),


# WIthout recursion


# def fibonacci(n):
#     first_elem = 0
#     second_elem = 1
#     count = 2
#     nums = [0, 1]
#     while count < n:
#         first_elem, second_elem = second_elem, first_elem + second_elem
#         nums.append(second_elem)
#         count += 1
#     return nums
