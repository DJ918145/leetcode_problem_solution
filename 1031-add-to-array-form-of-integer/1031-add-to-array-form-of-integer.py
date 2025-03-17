class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        a = ""
        ans = [] 
        for i in num:
            a = a + str(i)
        a = str(int(a)+k)
        for i in range(len(a)):
            ans.append(int(a[i]))
        return ans
        