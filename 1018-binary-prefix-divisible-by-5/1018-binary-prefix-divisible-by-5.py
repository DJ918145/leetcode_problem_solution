class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        output = []
        result = []
        val = 0
        for x in nums:
            val = (val*2+x)%5
            if val == 0:
                result.append(True)
            else:
                result.append(False)
        return result
