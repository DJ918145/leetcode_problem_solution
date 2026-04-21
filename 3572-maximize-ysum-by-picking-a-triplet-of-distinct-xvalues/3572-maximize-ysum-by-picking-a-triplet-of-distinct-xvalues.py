import heapq

class Solution(object):
    def maxSumDistinctTriplet(self, x, y):
        """
        :type x: List[int]
        :type y: List[int]
        :rtype: int
        """
        maxValues = {}
        for currX, currY in zip(x, y):
            if currX not in maxValues:
                maxValues[currX] = currY
            else:
                if currY > maxValues[currX]:
                    maxValues[currX] = currY
        vals = maxValues.values()
        if len(vals) < 3:
            return -1
        return sum(heapq.nlargest(3, vals))
