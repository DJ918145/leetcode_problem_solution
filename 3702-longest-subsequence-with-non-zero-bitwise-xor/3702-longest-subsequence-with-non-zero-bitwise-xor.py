class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        has_nonzero = False
        for n in nums:
            total_xor ^= n
            if n > 0:
                has_nonzero = True
        if total_xor != 0:
            return len(nums)
        elif has_nonzero:
            return len(nums) - 1
        else:
            return 0
