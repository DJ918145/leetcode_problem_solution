class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = 0  # keeps track of consecutive zeros
        
        for num in nums:
            if num == 0:
                count += 1      # extend the current zero-subarray
                ans += count    # add new subarrays ending here
            else:
                count = 0       # reset if non-zero found
                
        return ans
