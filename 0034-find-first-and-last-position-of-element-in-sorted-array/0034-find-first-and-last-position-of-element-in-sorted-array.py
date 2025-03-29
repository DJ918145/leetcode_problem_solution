class Solution(object):
    def searchRange(self, nums, target):
        ans = [-1, -1]
        # new = True
        for i in range(len(nums)):
            if nums[i] == target:
                if ans[0]==-1:
                    ans[0] = ans[1] = i
                    # new = False
                else:
                    ans[1] = i
        return ans
        