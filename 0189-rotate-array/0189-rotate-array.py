class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  # Handle cases where k > len(nums)
        rotated_arr = nums[-k:] + nums[:-k]  # Rotate array efficiently
        nums[:] = rotated_arr
        