class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        positive = [x for x in nums if x>=0]
        neative = [x for x in nums if x<0]
        for i, j in zip(positive, neative):
            answer.extend([i, j])

        return answer
        