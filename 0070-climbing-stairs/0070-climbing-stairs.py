class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Initialize variables for the first two steps
        first = 1
        second = 2

        # Iteratively calculate ways for steps from 3 to n
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
        
        return second
