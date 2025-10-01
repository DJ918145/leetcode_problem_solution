class Solution(object):
    def numWaterBottles(self, numB, numE):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drinked_bottle = 0
        while True:
            if numB>=numE:
                drinked_bottle += numE
                numB = numB + 1 - numE
            else:
                drinked_bottle += numB
                return drinked_bottle
        