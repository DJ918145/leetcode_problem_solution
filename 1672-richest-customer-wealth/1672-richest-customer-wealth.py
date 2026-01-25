class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(accounts)):
            ans = max(sum(accounts[i]), ans)
        return ans
        