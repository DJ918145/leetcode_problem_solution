class Solution:
    def removePalindromeSub(self, s):
        return int(s==s[::-1]) or 2