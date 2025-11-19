class Solution(object):
    def findMissingAndRepeatedValues(self, nums):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        my_dict = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i][j] not in my_dict:
                    my_dict[nums[i][j]]=1
                else:
                    my_dict[nums[i][j]]+=1
        a = -1
        b = -1
        for i in range(1, len(nums)**2 + 1):
            if i not in my_dict:
                b = i
            elif my_dict[i]==2:
                a = i
        return [a, b]
        