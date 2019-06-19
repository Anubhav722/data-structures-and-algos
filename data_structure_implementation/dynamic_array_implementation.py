# Check for the no. of bytes being actually held by the array as it grows.
# Example Usage (in shell):

# import sys
# from dynamicarray import DynamicArray
# arr = DynamicArray()
# arr.append(1)
# len(arr)
# arr.append(2)
# len(arr)
# sys.getsizeof(arr)
# arr.append(3)
# len(arr)
# sys.getsizeof(arr) # Note how the bytes taken by the array increases.

# Conclusion:
# This explains that when arrays get full they double in size and 
# hence increasing the no. of bytes occupied

import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0 # count of the no. of elements in the initial array
        self.capacity = 1
        self.A = self.make_array(self.capacity) # initial array

    def __len__(self):
        """
        Returns no. of elements in the array.
        """
        return self.n

    def __getitem__(self, k):
        """
        Returns element at index k.
        """
        if not 0 <= k < self.n:
            return IndexError("K index out of bounds")
        return self.A[k]

    def append(self, element):
        """
        Appends an element at the end of the array.
        """
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if the capacity isn't enough.

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):
        """
        Resize the array when no. of elements are equal to capacity.
        Uses `B` as a temporary array. 
        """
        B = self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]
        
        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        """
        Creates a new array in accordance to the new capacity of the new array.
        """
        return (new_capacity * ctypes.py_object)()
