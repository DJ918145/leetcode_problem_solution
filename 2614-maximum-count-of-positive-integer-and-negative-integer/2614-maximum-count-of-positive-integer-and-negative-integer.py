class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive = negative = 0
        for i in nums:
            if i>0:
                positive += 1
            elif i<0:
                negative += 1
            else:
                pass
        if positive > negative:
            return positive
        else:
            return negative