class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxi = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies>=maxi
                
        # ans = [True if candy >= maxi else False for candy in candies]
        
        return candies
        