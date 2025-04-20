class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        tank = curr = start = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            curr += g - c
            if curr < 0:
                start = i + 1
                curr = 0

        return start if tank >= 0 else -1