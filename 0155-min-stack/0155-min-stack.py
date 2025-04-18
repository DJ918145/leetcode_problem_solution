class MinStack(object):

    def __init__(self):
        self.ans = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.ans.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.ans = self.ans[:len(self.ans)-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.ans[-1]      

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.ans)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()