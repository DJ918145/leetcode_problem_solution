class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=2:
            return False
        sum = 0
        for i in range(len(nums)-2):
            sum = nums[i] + nums[i+1]
            for j in range(i+1, len(nums)-1):
                if nums[j] + nums[j+1] == sum:
                    return True
        return False        