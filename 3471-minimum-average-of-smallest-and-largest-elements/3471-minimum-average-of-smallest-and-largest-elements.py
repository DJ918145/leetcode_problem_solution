class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        min_avg = float('inf')
        nums.sort()
        for i in range(len(nums)/2):
            min_avg = min(min_avg, (nums[i] + nums[-1-i])/2.0)
        return min_avg
        