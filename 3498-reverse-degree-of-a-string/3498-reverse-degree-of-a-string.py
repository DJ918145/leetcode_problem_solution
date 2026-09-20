class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        reverse_degree = 0
        for i in range(len(s)):
            reverse_degree += (i+1)*(26-(ord(s[i])-ord("a")))
        return reverse_degree
        