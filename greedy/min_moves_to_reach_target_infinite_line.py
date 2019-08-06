# https://www.geeksforgeeks.org/find-minimum-moves-reach-target-infinite-line/

# Python 3 program to find minimum
# moves to reach target if we can
# move i steps in i-th move.


def reachTarget(target):

    # Handling negatives by symmetry
    target = abs(target)

    # Keep moving while sum is
    # smaller or difference is odd.
    sum = 0
    step = 0
    while (sum < target or (sum - target) % 2 != 0):
        step = step + 1
        sum = sum + step

    return step


# Driver code
target = 5
print(reachTarget(target))


# This code is contributed by Nikita Tiwari

