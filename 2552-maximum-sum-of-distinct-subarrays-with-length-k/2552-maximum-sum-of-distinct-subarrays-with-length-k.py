class Solution(object):
    def maximumSubarraySum(self, nums, k):
        mp = {}
        n = len(nums)
        ans, sum, i = 0, 0, 0
        for j in range(n):
            sum += nums[j]
            if nums[j] in mp:
                mp[nums[j]] += 1
            else:
                mp[nums[j]] = 1
            if j - i + 1 == k:
                if len(mp) == k:
                    ans = max(ans, sum)
                sum -= nums[i]
                mp[nums[i]] -= 1
                if not mp[nums[i]]:
                    del mp[nums[i]]
                i += 1
        return ans