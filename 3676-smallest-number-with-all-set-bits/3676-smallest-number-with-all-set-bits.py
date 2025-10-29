class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # binary = bin(n)[2:]
        # ans = '1'*len(binary)
        return int('1'*(len(bin(n))-2),2)