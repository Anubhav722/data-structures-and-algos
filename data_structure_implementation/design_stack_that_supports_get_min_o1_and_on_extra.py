# Solution:
# Use two stacks, one to store actual stack elements and other as an auxillary stack to
# store min. values. The idea is to do push() and pop() operations in such a way that the top
# of auxillary stack is always the minimum.


class SpecialStack:
    def __init__(self):
        self.s1 = []
        self.s2 = [] # min stack

    def push(self, x):
        if not self.s1:
            self.s1.append(x)
            self.s2.append(x)

        else:
            self.s1.append(x)
            if self.s1[-1] < self.s2[-1]:
                self.s2.append(x)
            else:
                self.s2.append(self.s2[-1])

    def pop(self):
        self.s1.pop()
        self.s2.pop()

    def getMin(self):
        return self.s2[-1]
