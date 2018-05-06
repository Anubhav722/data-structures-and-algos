class Solution2:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        anagrams = {}
        for i in xrange(len(A)):
            key = ''.join(sorted(A[i]))
            if key in anagrams:
                anagrams[key].append(i+1)
            else:
                anagrams[key] = [i+1]
        for key in anagrams:
            if len(anagrams[key]) < 1:
                del anagrams[key]
        return [i for i in anagrams.itervalues()]

# My Solution. which arguably used a lot more space.


class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        sorted_lists = []
        ans = []
        indexes = []
        for i in A:
            sorted_lists.append(sorted(i))
        for i in range(len(sorted_lists)):
            c = i
            if i in indexes:
                continue
            elif sorted_lists[i] in sorted_lists[c+1:]:
                while sorted_lists[i] in sorted_lists[c+1:]:
                    indexes.append(i)
                    b = sorted_lists[i+1:].index(sorted_lists[i])+(i+1)
                    indexes.append(b)
                    ans.append([i+1,b+1])
                    c = b+1
            else:
                ans.append([i+1])
        return ans