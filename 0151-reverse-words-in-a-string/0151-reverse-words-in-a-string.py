class Solution(object):
    def reverseWords(self, s):
        # s = s.split()
        s = list(s.split())[::-1]
        s=" ".join(s)
        return s