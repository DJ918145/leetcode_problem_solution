class Solution(object):
    def countSubarrays(self, nums, k):
        n = len(nums)
        i = 0
        sum_ = 0
        cnt = 0
        for j in range(n):
            sum_ += nums[j]
            while i <= j and sum_ * (j - i + 1) >= k:
                sum_ -= nums[i]
                i += 1
            cnt += (j - i + 1)
        return cnt