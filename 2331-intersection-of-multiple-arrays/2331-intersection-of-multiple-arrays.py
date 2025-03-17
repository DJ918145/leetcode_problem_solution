class Solution(object):
    def intersection(self, nums):
        ans = nums[0]
        for i in range(len(nums)):
            if len(nums[i])<=len(ans):
                ans= nums[i]
        for i in range(len(nums)):
            j = 0
            while len(ans)>j:
                if ans[j] in nums[i]:
                    j = j + 1
                else:
                    ans.pop(j)
        ans.sort()
        return ans
        