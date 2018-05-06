
def binarySearch(A, n, x):
    low = 0
    high = n - 1
    result = -1

    while (low <= high):
        mid = (low + high) / 2

        if x == A[mid]:
            result = mid
            high = mid - 1 # to find the first occurence of the element in the array.
            # low = mid + 1 to find the last occurence of the element in the array.
        elif x < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result
