class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        front = self.s1[0]
        self.s2 = self.s1[1:]
        self.s1 = self.s2
        return front

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0
