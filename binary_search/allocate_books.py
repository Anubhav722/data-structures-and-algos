class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def func(self, A, B, pgs):
        # import ipdb; ipdb.set_trace()
        if pgs < max(A):
            return 0
        cur_sum = 0
        c = 0
        for pg in A:
            if cur_sum + pg <= pgs:
                cur_sum += pg
            else:
                c += 1
                if c >= B:
                    return 0
                cur_sum = pg
        return 1

    def books(self, A, B):
        if len(A) < B:
            return -1
        low = min(A)
        high = sum(A)
        res = -1
        while low <= high:
            mid = (low + high) / 2
            t = self.func(A, B, mid)
            # print mid, low, high
            if t:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
