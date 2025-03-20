class Solution(object):
    def isPalindrome(self, s):
        s= ''.join(filter(str.isalnum, str(s))).lower()
        return True if s == s[::-1] else False