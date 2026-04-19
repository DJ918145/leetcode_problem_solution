class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        return abs(n - _reverse(n))
        
def _reverse(n):
    digits = [digit for digit in str(n)]
    return int("".join(digits[::-1]))