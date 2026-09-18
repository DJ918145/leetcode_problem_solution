class Solution:
    def minOperations(self, nums, numsDivide):
        # Find GCD without using math.gcd
        g = numsDivide[0]

        for x in numsDivide[1:]:
            while x != 0:
                g, x = x, g % x

        # Sort nums
        nums.sort()

        # Find the first number that divides the GCD
        for i in range(len(nums)):
            if g % nums[i] == 0:
                return i

        return -1