class Solution(object):
    def findDisappearedNumbers(self, nums):
        s=set(nums)
        l=[]
        for i in range( 1,len(nums)+1):
            if i not in s:
                l.append(i)
        return l