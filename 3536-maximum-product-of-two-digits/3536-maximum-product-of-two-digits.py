class Solution(object):
    def maxProduct(self, n):
        first_maxi, second_maxi = 0, 0
        while n>0:
            c = n%10
            if c >= first_maxi:
                second_maxi = first_maxi
                first_maxi = c
            elif c >= second_maxi and c <= first_maxi:
                second_maxi = c
            n//=10
        return first_maxi * second_maxi



        """
        :type n: int
        :rtype: int
        """
        