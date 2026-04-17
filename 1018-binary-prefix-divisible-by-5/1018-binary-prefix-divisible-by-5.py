class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        binary = ""
        ans = []
        for i in nums:
            binary += str(i)
            if(int(binary, 2)%5==0):
                ans.append(True)
            else:
                ans.append(False)
        return ans
