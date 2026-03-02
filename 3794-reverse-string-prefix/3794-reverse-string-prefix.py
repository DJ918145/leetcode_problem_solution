class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k>= len(s):
            return s[::-1]
        elif k == 1:
            return s
        else:
            answer = s[:k][::-1] + s[k:]
            return answer
