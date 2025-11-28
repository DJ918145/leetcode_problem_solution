class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return len(nums)
        elif 1 not in nums:
            return 0
        maxi = 0
        countinous = 0
        for i in range(len(nums)):
            if nums[i]!=1:
                maxi = max(maxi, countinous)
                countinous=0
            else:
                countinous += 1
        maxi = max(maxi, countinous)
        return maxi        