class Solution(object):
    def maxProduct(self, n):
        first_maxi, second_maxi = 0, 0
        for cr in str(n):
            c = int(cr)
            if c >= first_maxi:
                second_maxi = first_maxi
                first_maxi = c
            elif c >= second_maxi and c <= first_maxi:
                second_maxi = c
        return first_maxi * second_maxi



        """
        :type n: int
        :rtype: int
        """
        