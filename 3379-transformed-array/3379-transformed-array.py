class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newArr = []
        for i in range(len(nums)):
            newArr.append(nums[(nums[i]+i)%len(nums)])
        return newArr