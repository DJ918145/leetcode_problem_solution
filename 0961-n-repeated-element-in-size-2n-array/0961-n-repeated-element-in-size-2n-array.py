class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        repeted = 0
        answer = 0
        for i in set(nums):
            if nums.count(i)>repeted:
                answer = i
                repeted = nums.count(i)
        return answer