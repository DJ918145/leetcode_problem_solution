class Solution(object):
    def moveZeroes(self, nums):
        for i in nums:
            if i ==0:
                nums.remove(0)
                nums.append(0)        