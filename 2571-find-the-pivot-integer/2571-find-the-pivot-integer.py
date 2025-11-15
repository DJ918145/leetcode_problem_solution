class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = (n*(n+1)//2)**0.5
        return int(ans) if ans == int(ans) else -1