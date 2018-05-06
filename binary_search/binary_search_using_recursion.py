

def binarySearch(arr, low, high, x):

    if low > high:
        return -1

    mid = low + (high - low) / 2

    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binarySearch(arr, mid + 1, high, x)
    else:
        return binarySearch(arr, low, mid - 1, x)
