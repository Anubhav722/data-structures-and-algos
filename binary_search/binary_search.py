class BinarySearch:

    def __init__(self, A):
        """
        Takes array A as input.
        Assuming array A is sorted.
        """
        self.arr = A
        self.n = len(A)

    def search(self, x):
        """
        Searches for element x in array A using binary search
        Returns index if element is found, else -1.
        """
        start = 0
        end = self.n - 1

        while (start <= end):
            mid = (start + end) / 2

            # To be in the range of 32 bit signed integer.
            # Use the below code to prevent overflow.
            # (start+end) can cause overflow.
            # mid = start + (end-start)/2

            if self.arr[mid] == x:
                return mid
            elif self.arr[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        print start, end
        return -1
