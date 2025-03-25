class Solution(object):
    def productExceptSelf(self, nums):
        ans = []
        total_product = 1
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        for num in nums:
            if num != 0:
                total_product *= num
        for num in nums:
            if zero_count == 0:
                ans.append(total_product // num)
            elif num == 0:
                ans.append(total_product)
            else:
                ans.append(0)
        return ans