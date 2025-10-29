class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(''.join(sorted(s)))
        t = list(''.join(sorted(t)))
        for char1 in s:
            if char1 not in t[0]:
                return t[0]
            else:
                t = t[1:]
        return t[0]
        
        