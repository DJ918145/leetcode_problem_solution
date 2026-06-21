class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        expense = 0
        costs.sort()
        for i in range(len(costs)):
            if coins < costs[i]:
                return i
            else:
                coins = coins-costs[i]
        return len(costs)
