class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        val = 0
        ans = []
        for i in nums:
            val = (val*2+i)%5
            if val==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
