class Solution(object):
    def numWaterBottles(self, numB, numE):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drinked_bottle = numB
        while True:
            if numB>=numE:
                new_bottles = numB//numE
                numB = numB%numE
                drinked_bottle += new_bottles
                numB = numB % numE + new_bottles
            else:
                # drinked_bottle += numB
                return drinked_bottle
        