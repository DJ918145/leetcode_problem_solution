class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        while True:
            if len(set(nums)) == len(nums) or len(nums) == 0:
                return count
            else:
                nums = nums[3:]
                count += 1
        