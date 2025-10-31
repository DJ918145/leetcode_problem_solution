class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for i in nums:
            if nums.count(i)==2 and i not in answer:
                answer.append(i)
        return answer