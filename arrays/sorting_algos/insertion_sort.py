# Slightly better than bubble sort and selection sort

# Best Case: O(n)
# Worst Case: O(n^2)
# Average Case: O(n^2)


def insertion_sort(arr, n):
    for i in range(n):
        value = arr[i]
        hole = i

        while (hole > 0 and arr[hole - 1] > value):
            arr[hole] = arr[hole - 1]
            hole = hole - 1

        arr[hole] = value
