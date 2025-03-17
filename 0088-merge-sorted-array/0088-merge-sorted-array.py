class Solution(object):
    def merge(self, arr1, m, arr2, n):
        for i in range(n):
            arr1[m+i] = arr2[i]
        arr1.sort()