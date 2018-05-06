
def findCount(A, x, searchFirst):
    n = len(A)
    high = n - 1
    low = 0

    result = -1
    while (low <= high):
        mid = (high + low) / 2
        if A[mid] == x:
            # return mid
            result = mid
            if searchFirst:
                # to find first occurence
                high = mid - 1
            else:
                low = mid + 1
        elif A[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result


def findOccurences(A, x):
    first_occurence = findCount(A, x, True)

    if first_occurence == -1:
        print "Not Found"
        return -1
    else:
        last_occurence = findCount(A, x, False)
    count = (last_occurence - first_occurence) + 1
    return count
