class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        dummy = []
        for i in nums1:
            if i not in nums2:
                dummy.append(i)
        answer.append(dummy)
        dummy = []
        for j in nums2:
            if j not in nums1:
                dummy.append(j)
        answer.append(dummy)
        return answer