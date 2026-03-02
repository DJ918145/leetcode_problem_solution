class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k==1:
            return s
        m=s[0:k][::-1]+s[k:]
        return m