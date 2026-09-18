class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff,n=0,sorted(set(nums))
        for i in range(len(n)-1):
            if n[i+1]-n[i] > diff:
                diff = n[i+1] - n[i]
        return(diff)        