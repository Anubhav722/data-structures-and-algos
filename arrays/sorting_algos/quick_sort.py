# Average Case: O(nlogn)
# Worst Case: O(n^2)

# In place algorithm

# Worst Case scenario of quick sort algo is almost avoided
# by using what we call a randomized version of quick sort.

# We select a random element called pivot.
# Then we rearrange the array such that all the elements lesser than it
# are towards the left and greater elements are towards the right of the pivot.

# for ex.

# 7, 2, 1, 6, 8, 5, 3, 4 -------> 2, 1, 3, 4, 8, 5, 7, 6
                     # |                   |
                     # pivot               pivot

# In this case we are taking the rightmost element as the pivot.

def partition(arr, start_index, end_index):
    pivot = arr[end_index]
    partition_index = start_index

    for i in range(start_index, end_index):
        if arr[i] <= pivot:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index += 1
    arr[partition_index], arr[end_index] = arr[end_index], arr[partition_index]
    return partition_index


def quick_sort(arr, start_index, end_index):

    if (start_index >= end_index):
        return

    pivot_index = partition(arr, start_index, end_index)

    # Making a recursive call
    quick_sort(arr, start_index, pivot_index-1)
    quick_sort(arr, pivot_index, end_index)
    return arr

# quick_sort(arr, 0, len(arr))
