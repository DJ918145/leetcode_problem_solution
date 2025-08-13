class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        for i in range(100):
            if 3**i == n:
                return True
            if 3**i>=n:
                return False
        return False        