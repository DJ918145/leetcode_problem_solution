class Solution(object):
    def isPalindrome(self, n, d):
        st = ''
        while n>0:
            st+= str(n%d)
            n//=d
        return True if st==st[::-1] else False
    def isStrictlyPalindromic(self, n):
        for i in range(2,n+1):
            if(self.isPalindrome(n, i)==False):
                return False
        return True