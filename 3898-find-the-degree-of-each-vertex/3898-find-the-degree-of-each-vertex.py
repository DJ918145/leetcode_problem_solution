class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for mat in matrix:
            result.append(mat.count(1))
        return result
        