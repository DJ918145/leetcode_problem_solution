class Solution(object):
    def largestAltitude(self, nums):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans = [0]
        for i in nums:
            # answer = ans[-1] + i
            ans.append(ans[-1] + i)
        return max(ans)
        