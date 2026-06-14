import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = [str(i) for i in range(1, n + 1)]
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
            
        k -= 1
        result = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            
            result.append(numbers.pop(idx))
            k %= factorials[i]
            
        return "".join(result)