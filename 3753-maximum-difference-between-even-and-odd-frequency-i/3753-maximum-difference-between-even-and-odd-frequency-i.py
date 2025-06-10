class Solution:
    def maxDifference(self, s):
        from collections import Counter
        freq = Counter(s)
        odd = float('-inf')
        even = float('inf')
        for count in freq.values():
            if count == 0:
                continue
            if count % 2 == 0:
                even = min(even, count)
            else:
                odd = max(odd, count)
        return odd - even