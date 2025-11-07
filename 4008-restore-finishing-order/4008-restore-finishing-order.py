class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        answer = []
        for num in order:
            if num in friends:
                answer.append(num)
        return answer