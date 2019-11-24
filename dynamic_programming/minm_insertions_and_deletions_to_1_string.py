# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m27OkE8D08O

def minm_insertions_deletions(s1, s2):
	c = recur(s1, s2, 0, 0)
	# assuming s1 is always the bigger string
	print ("minm deletions", len(s1) - c)
	print ("minm insertions", len(s2) - c)


def recur(s1, s2, i1, i2):
	if i1 == len(s1) or i2 == len(s2):
		return 0
	if s1[i1] == s2[i2]:
		return 1 + recur(s1, s2, i1 + 1, i2 + 1)

	c1 = recur(s1, s2, i1 + 1, i2)
	c2 = recur(s1, s2, i1, i2 + 1)
	return max(c1, c2)
