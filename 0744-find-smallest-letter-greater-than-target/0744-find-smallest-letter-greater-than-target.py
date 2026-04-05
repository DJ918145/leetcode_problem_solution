class Solution:
    def nextGreatestLetter(self, L, target):
        i=bisect_right(L, target)
        return L[i] if i<len(L) else L[0]