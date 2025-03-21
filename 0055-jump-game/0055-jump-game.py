class Solution(object):
    def canJump(self, nums):
        max_reac = 0
        for i in range(len(nums)):
            if i > max_reac:
                return False
            max_reac = max(max_reac, i+nums[i])
        return True

        