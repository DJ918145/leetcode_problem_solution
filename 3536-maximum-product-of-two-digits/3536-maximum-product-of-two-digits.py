class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = []
        for c in str(n):
            number.append(int(c))
        number.sort()
        return number[-1]*number[-2]