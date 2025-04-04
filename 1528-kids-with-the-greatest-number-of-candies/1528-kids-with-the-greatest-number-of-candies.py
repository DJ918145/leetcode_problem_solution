class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxi = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies >= maxi
        return candies
        