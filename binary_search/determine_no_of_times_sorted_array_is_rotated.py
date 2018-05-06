# There are no duplicates in the array.

# Case 1: A[low] <= A[high]
#         return low
# next --> (mid + 1) % N
# prev --> (mid + N - 1) % N

# Case 2: A[mid] <= A[next] and A[mid] <= A[prev]
#         return mid

# Case 3: A[mid] <= A[high]
          # high = mid - 1

# Case 4: A[mid] >= A[low]
#         low = mid + 2


def findRotationCount(A):
    n = len(A)
    low = 0
    high = n - 1

    while (low <= high):
        if (A[low] <= A[high]):  # Case 1
            return low

        mid = (low + high) / 2
        _next = (mid + 1) % n
        prev = (mid + n - 1) % n

        if (A[mid] <= A[_next] and A[mid] <= A[prev]):  # Case 2
            return mid

        elif (A[mid] <= A[high]):  # Case 3
            high = mid - 1
        elif (A[mid] >= A[low]):  # Case 4
            low = mid + 1

    return -1
