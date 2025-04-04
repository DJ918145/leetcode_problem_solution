class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxi = max(candies)
        for i in range(len(candies)):
            candies[i] += extraCandies
        ans = [True if candy >= maxi else False for candy in candies]
        # for candy in candies:
        #     if candy >= maxi:
        #         ans.append(True)
        #     else:
        #         ans.append(False)

        return ans
        