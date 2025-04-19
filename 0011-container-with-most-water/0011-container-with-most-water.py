class Solution(object):
    def maxArea(self, nums):
        area = 0
        l , r = 0, len(nums) - 1

        while l < r:
            ans = abs(l - r) * min(nums[l], nums[r])
            area = max(area, ans)
            if nums[l] <= nums[r]:
                l += 1
            else:
                r -= 1
        return area