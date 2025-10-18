class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        set_arr = set(arr)
        occ = []
        for i in set_arr:
            occ.append(arr.count(i))
        set_occ = set(occ)
        return True if len(occ) == len(set_occ) else False
        