# Selection sort is the simplest form of sorting.

# We create a new empty array of the same size as the original array.
# We fetch/remove the minimum element from the original array and place it in empty array on 0th index.
# We then repeat the process again and again.

# This is not an in-place sorting algorithm.
# An in-place sorting algorithm takes constant amount of extra memory.

# We can make this algo in-place in the following manner.
# We can search the minimum element in the array and swap it with element at 0th index.
# Then repeat the process.


# Time Complexity of this algorithm is O(n^2)

def selection_sort(arr, n):

    for i in range(n):
        min_element = min(arr[i:])
        min_element_index = arr[i:].index(min_element) + i

        # Perform swapping
        temp = arr[i]
        arr[i] = min_element
        arr[min_element_index] = temp

    return arr
