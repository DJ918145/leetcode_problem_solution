class Solution(object):
    def reverseWords(self, s):
        # s = s.split()
        return " ".join(list(s.split())[::-1])
        # s=" ".join(s)
        # return s