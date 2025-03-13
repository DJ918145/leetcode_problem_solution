class Solution(object):
    def removeElement(self, arr, tar):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        size = len(arr)
        for i in range(size):
            if arr[i] == tar:
                count = count + 1
        for i in range(count):
            arr.remove(tar)
            arr.append('_')
        return size-count