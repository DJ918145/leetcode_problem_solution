class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        while n > 0:
            n //= 5  # Integer division by 5
            count += n  # Count factors of 5
        return count