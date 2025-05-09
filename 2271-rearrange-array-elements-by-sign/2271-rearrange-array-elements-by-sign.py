class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive = [x for x in nums if x>=0]
        neative = [x for x in nums if x<0]
        nums = []
        for i, j in zip(positive, neative):
            nums.extend([i, j])

        return nums
        