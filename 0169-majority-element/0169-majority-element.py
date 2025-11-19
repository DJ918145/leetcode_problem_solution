class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets = set(nums)
        for i in sets:
            if nums.count(i)> len(nums)//2:
                return i
        