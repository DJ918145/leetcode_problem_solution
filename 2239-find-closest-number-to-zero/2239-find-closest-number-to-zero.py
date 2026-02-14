class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        for i in nums:
            if abs(i) < abs(ans) or (abs(i) == abs(ans) and i > ans):
                ans = i
        return ans