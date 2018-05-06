# Worst Case: O(nlogn)


# Divide and Conquer algorithms
# Recursive algorithm
# Stable sorting algorithm
# Not an in place sorting algorithm


# Space complexity: O(n)

def merge_array(left_array, right_array, arr):
    length_left_array = len(left_array)
    length_right_array = len(right_array)
    i = 0  # marks the smallest unpicked in left array
    j = 0  # marks the smallest unpicked in right aray
    k = 0  # marks the index of the position that needs to be filled.

    while i < length_left_array and j < length_right_array:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            k += 1
            i += 1
        else:
            arr[k] = right_array[j]
            k += 1
            j += 1

    while i < length_left_array:
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < length_right_array:
        arr[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return

    mid = n / 2
    left_array = arr[:mid]
    right_array = arr[mid:]

    merge_sort(left_array)
    merge_sort(right_array)

    merge_array(left_array, right_array, arr)
