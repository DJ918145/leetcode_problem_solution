class Solution(object):
    def hIndex(self, nums):
        """
        :type citations: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)
        for i, c in enumerate(nums):
            if c<=i:
                return i
        return len(nums) 