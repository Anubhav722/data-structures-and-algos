# https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/

def josephus(n, k):
    if n == 1:
        return 1

    else:
        return (josephus(n-1, k) + k-1)  % n + 1
