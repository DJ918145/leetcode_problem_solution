class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ori = n
        sum_of_digit, product_of_digit = 0, 1
        while n>0:
            r = n %10
            sum_of_digit += r
            product_of_digit *= r
            n //=10
        return True if (ori % (sum_of_digit+product_of_digit)) == 0 else False