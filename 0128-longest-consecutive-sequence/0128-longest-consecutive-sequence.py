class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        answer = [0]
        count = 1
        nums = sorted(set(nums))
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                count += 1 
            else:
                answer.append(count)
                count = 1
        return max(max(answer),count)
        