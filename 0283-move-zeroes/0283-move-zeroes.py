class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        i=0
        while i != len(nums):
            if nums[i] == 0:
                count += 1
                nums.remove(0)
            else:
                i += 1
        for _ in range(count):
            nums.append(0)