# https://www.geeksforgeeks.org/queue-using-stacks/


class Queue:
    def __self__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        # Move all the elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
            # push item into self.s1
        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        # if first stack is empty
        if len(self.s1) == 0:
            print ("Q is empty")

        # return top of self.s1
        x = self.s1[-1]
        self.s1.pop()
        return x
