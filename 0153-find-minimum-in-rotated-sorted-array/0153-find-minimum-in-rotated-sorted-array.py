class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_index = nums.index(max(nums))
        nums_rotated = len(nums)-max_index
        return min(nums)