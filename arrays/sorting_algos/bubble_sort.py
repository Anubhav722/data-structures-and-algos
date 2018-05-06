# We compare the adjacent elements

# Time complexity : O(n^2)

# Best Case: O(n)
# Average Case: O(n^2)
# Worst Case: O(n^2)


def bubble_sort(arr, n):

    for k in range(n):
        flag = 0
        for i in range(n - k - 1):
            if arr[i] > arr[i + 1]:
                # Swapping
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = 1

        if flag == 0:
            break
