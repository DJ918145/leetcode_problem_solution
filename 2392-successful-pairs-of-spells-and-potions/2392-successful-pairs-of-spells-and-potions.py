class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        ans = []
        m = len(potions)
        def searc(spell):
            l , r = 0, m-1
            while l<=r:
                mid = (l + r)// 2
                if spell*potions[mid]>=success:
                    r= mid - 1
                else:
                    l = mid + 1
            return m - l
        for spell in spells:
            ans.append(searc(spell))
        return ans
        