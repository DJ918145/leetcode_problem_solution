class Solution(object):
    def findMissingAndRepeatedValues(self, nums):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        arr = []
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                arr.append(nums[i][j])
        for i in arr:
            if arr.count(i)==2:
                ans.append(i)
                break
        for i in range(1,len(arr)+1):
            if i not in arr:
                ans.append(i)
        return ans
        