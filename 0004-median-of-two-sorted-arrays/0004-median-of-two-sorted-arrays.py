class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        
        size = len(nums1)
        if size%2 == 0:
            i = size / 2
            num = float(nums1[i-1]+nums1[i])
            return num/2
        else:
            i = size / 2
            return float(nums1[i])
        