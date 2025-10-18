class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occ = []
        for i in set(arr):
            occ.append(arr.count(i))
        return True if len(occ) == len(set(occ)) else False
        