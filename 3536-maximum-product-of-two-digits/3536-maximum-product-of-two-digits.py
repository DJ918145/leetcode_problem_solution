class Solution(object):
    def maxProduct(self, n):
        first_maxi, second_maxi = 0, 0
        for c in str(n):
            if int(c) >= first_maxi:
                second_maxi = first_maxi
                first_maxi = int(c)
            elif int(c) >= second_maxi and int(c) <= first_maxi:
                second_maxi = int(c)
        return first_maxi * second_maxi



        """
        :type n: int
        :rtype: int
        """
        