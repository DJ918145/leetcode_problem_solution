class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxi = max(candies)
        for i in range(len(candies)):
            # candies[i] += extraCandies
            if candies[i] + extraCandies>=maxi:
                candies[i] = True
            else:
                candies[i] = False
        # ans = [True if candy >= maxi else False for candy in candies]
        
        return candies
        