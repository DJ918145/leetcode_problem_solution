class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        missing = []
        for i in range(len(arr)+k+1):
            if i not in arr:
                missing.append(i)
        return missing[k]
        