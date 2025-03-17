class Solution(object):
    def thirdMax(self, nums):
        nums=sorted(set(nums))
        if len(nums)<3:
            return nums[-1]
        
        else:
            return nums[-3]
        