class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        def is_symmetric(x):
            s = str(x)
            n = len(s)
            # Symmetry is only possible if the number has an even number of digits
            if n % 2 != 0:
                return False
            half = n // 2
            # Check if the sum of the first half equals the sum of the second half
            return sum(int(d) for d in s[:half]) == sum(int(d) for d in s[half:])
        
        # Iterate through the range and count symmetric integers
        count = 0
        for num in range(low, high + 1):
            if is_symmetric(num):
                count += 1
        return count

        