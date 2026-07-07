class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        value = ''
        digit_sum = 0

        for c in str(n):
            if c != '0':
                digit_sum += int(c)
                value += c

        if value == '':
            return 0

        return int(value) * digit_sum